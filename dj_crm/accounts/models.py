from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, full_name=None, is_active=True, is_staff=False, is_admin=False, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user_obj = self.model(
            email = self.normalize_email(email, **extra_fields)
        )
        user_obj.set_password(password)
        user_obj.full_name = full_name
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.save(using=self._db)
        return user_obj 

    def create_staffuser(self, email, password, full_name=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self._create_user(email, password=password, full_name=full_name, is_staff=True, **extra_fields)
        return user


    def create_superuser(self, email, password, full_name=None, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self._create_user(email, password=password, full_name=full_name, is_staff=True, is_admin=True,**extra_fields)       
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address',max_length=100, unique=True)
    full_name = models.CharField(verbose_name='Name', max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # super-user
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    # notice the absence of a "Password field", that is built in.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()    

    def __str__(self):
        return self.email

    def get_name(self):
        if self.full_name:
            return self.full_name
        return self.email     

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True    

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin    

         