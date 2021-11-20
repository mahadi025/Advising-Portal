from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, studentId, first_name, last_name, email, img=None, password=None):
        if not studentId:
            raise ValueError('Users must have an Student Id')
        user = self.model(
            email=self.normalize_email(email),
            studentId=studentId,
            first_name=first_name,
            last_name=last_name,
            img=img
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, studentId, img=None, email=None, first_name=None, last_name=None, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            studentId=studentId,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            img=img
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, studentId, img, email=None, first_name=None, last_name=None, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            studentId=studentId,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            img=img
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    img= models.ImageField(upload_to='pics',null=True,blank=True,default=0)
    studentId=models.CharField(max_length=13,unique=True,null=False)
    first_name=models.CharField(max_length=30,null=True,blank=True)
    last_name=models.CharField(max_length=30,null=True,blank=True)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'studentId'
    REQUIRED_FIELDS = [] 

    def get_full_name(self):
        # The user is identified by their email address
        return self.studentId

    def get_short_name(self):
        # The user is identified by their email address
        return self.studentId

    def __str__(self):
        return self.studentId

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
    objects = UserManager()