from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from .choices import STATUS

class User(AbstractBaseUser, PermissionsMixin):
    '''
        Custom user model
        returns -> email

        - email (char)
        - name (char)
        - is_active (boolean)
        - is_admin (boolean)
        - is_staff (boolean)
        - is_deleted (boolean)

    '''
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS, default="1")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


    

