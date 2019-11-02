from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class custommanager(BaseUserManager):
    def create_user(self,email,password=None,is_active=True,is_admin=False,is_staff=False):
        if not email:
            raise ValueError("Users are required to have an email.")

        if not password:
            raise ValueError('Users are required to have a password')
        user_obj=self.model(
        email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=is_active
        user_obj.save(using=self._db)
        return user_obj
    def create_staff(self,email,password=None):
        user=self.create_user(
        email,
        password=password,
        is_staff=True
        )
        return user
    def create_superuser(self,email,password=None):
        user=self.create_user(
        email,
        password=password,
        is_staff=True,
        is_admin=True
        )
        return user

class customuser(AbstractBaseUser):
    email=models.EmailField(max_length=255,unique=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    admin=models.BooleanField(default=False)
    staff=models.BooleanField(default=False)
    active=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=custommanager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff
