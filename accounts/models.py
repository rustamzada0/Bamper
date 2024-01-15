from django.db import models
from django.db.models.fields import CharField, BooleanField, EmailField, TextField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from core.models import AbstractModel
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.

class User(AbstractUser, AbstractModel):
    full_name = CharField(max_length=50, null=True, blank=True, default='')
    emailornumber = CharField(max_length=50, unique=True, null=True, blank=True, default='')
    username = CharField(max_length=30, null=True, blank=True, default='')
    password = CharField(max_length=255, null=True, blank=True, default='')
    is_store = BooleanField(default=False)
    image = ImageField(upload_to='user-media/', null=True, blank=True)
    description = TextField(null=True, blank=True)
    adress = CharField(max_length=255, null=True, blank=True, default='')
    map_link = CharField(max_length=255, null=True, blank=True, default='')
    makes = IntegerField(default=0)
    otp = models.CharField(max_length=6)

    # forget_pwd_token = CharField(max_length=100,null=True,blank=True)
    # email_confirmed = BooleanField(default=False)

    USERNAME_FIELD = 'emailornumber'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.emailornumber
    
    def save(self, *args, **kwargs):
        while User.objects.filter(username=self.username).exists():
            self.username = self.emailornumber.split('@')[0] + str(random.randint(100000, 999999))

        super(User, self).save(*args, **kwargs)
    