from django.db import models

# Model to store User Informations.

class UserInformation(models.Model):
    '''Stores informations for the user who choose personal account to use'''
    user_email=models.EmailField(null=False,blank=False,primary_key=True)
    user_full_name=models.CharField(null=False,blank=False,max_length=50)
    user_profile_picture=models.ImageField(null=True,blank=True,upload_to='user_profile_pictures/')
    user_contact_no=models.IntegerField(null=True,blank=True)
    user_address=models.CharField(null=True,blank=True,max_length=300)
    
    class Meta:
        verbose_name = "User Information"
    
    def __str__(self) -> str:
        return str(self.user_email)

    
    
    
