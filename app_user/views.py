from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

EMAIL_SIGNUP = 'email_signup'
SOCIAL_SIGNUP = 'social_signup'
# Create your views here.
class UserLogin(APIView):

    def post(self,request):

        #getting json data
        data = request.data
        #getting all credentials provided by user
        email = data.get('email')
        password = data.get('password')
        
        try:
            user_username = User.objects.get(email=email)
        except:
            user_username = None

        user = authenticate(username = user_username,password = password)

        if user is not None:
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'message':'Login Successful',
                'refresh':str(refresh_token),
                'access':str(refresh_token.access_token),
            },status= status.HTTP_200_OK)
        else:
            return Response(
                {'message':'Invalid Credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED)
        
@api_view(['POST'])
def UserRegistration(request,signup_method = None):

    if signup_method == EMAIL_SIGNUP:
        
        data = request.data
        # get username password and email
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if the username and email are already taken
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return Response({'Invalid': 'User Name Alreadt Exists. Try Loggin In'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Creating new u
        try:
            new_user = User.objects.create(username=username,email=email,password=password)
            new_user.save()
            return Response({'success': f'Signup Successful. Username, {username}, created'}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'Error': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        return Response(data)