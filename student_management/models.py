# Model for User Authentication

from django.db import models
from admin_dash.models import Course
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, regd_id, name, email, password):
        if not regd_id:
            raise ValueError("Candidate must have a Registration ID! Otherwise you're NOT PERMITTED to Give the Exam!")
        user = self.model(
            regd_id = regd_id,
            email=email,
            name=name,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, regd_id, name, email, password):
        user = self.create_user(
            regd_id,
            name,
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    regd_id = models.CharField(verbose_name='Registration ID', max_length=15, unique=True, null=True)
    name = models.CharField(verbose_name='Name', max_length=30, null=True)
    password = models.CharField(max_length=50, verbose_name='Password', unique=True)
    email = models.EmailField(max_length=50, verbose_name='Email Address', unique=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'regd_id'
    REQUIRED_FIELDS = ['name', 'email', 'password']
    objects = UserManager()

    def __str__(self) -> str:
        return self.name
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True