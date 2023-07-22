from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Account Manager that either creates a normal user, or a super user (admin)
class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
           raise ValueError("Username is missing")
        user = self.model(username=username, email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.superuser = True
        user.save(using=self._db)
        return user

# The User model within the Database, which is used for the Account System
class User(AbstractBaseUser):
    user_id         = models.AutoField(primary_key=True)
    username        = models.CharField(max_length=64, null=False, unique=True)
    first_name      = models.CharField(max_length=64, null=True)
    last_name       = models.CharField(max_length=64, null=True)
    email           = models.EmailField(max_length=128, null=False, unique=True)
    password        = models.CharField(max_length=256, null=False)
    superuser       = models.BooleanField(default=False)

    # Displays the Username of the User as the Database Record
    def __str__(self):
        return f"{self.username}"

    object = AccountManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'password',
    ]

