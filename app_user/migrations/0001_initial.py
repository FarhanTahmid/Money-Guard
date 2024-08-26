# Generated by Django 5.1 on 2024-08-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_full_name', models.CharField(max_length=50)),
                ('user_profile_picture', models.ImageField(blank=True, null=True, upload_to='user_profile_pictures/')),
                ('user_contact_no', models.IntegerField(blank=True, null=True)),
                ('user_address', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'User Information',
            },
        ),
    ]
