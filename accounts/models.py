# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    nickname = models.CharField(max_length = 200)
    mbti = models.CharField(max_length = 15)



# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, nickname, password=None):

#         user = self.model(
#             username=username,
#             nickname=nickname
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None):
#         user = self.create_user(
#             password=password,
#             username=username
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
        
        
# class User(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True)
#     nickname = models.CharField(max_length=255)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)


#     class Meta:
#         db_table = 'user'

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username']