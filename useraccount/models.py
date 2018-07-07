from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.CharField(max_length=32,unique=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    mobile = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.firstname
    class Meta:
        db_table = "User"

class UserAddress(models.Model):
    country = models.CharField(max_length=32)
    full_name = models.CharField(max_length=32)
    mobile = models.CharField(max_length=13)
    pincode = models.CharField(max_length=10)
    street_address = models.CharField(max_length=256)
    landmark = models.CharField(max_length=128)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    is_shipping = models.BooleanField()
    is_billing = models.BooleanField()
    is_default_shipping = models.BooleanField()
    is_default_billing = models.BooleanField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    class Meta:
        db_table = 'user_addresses'