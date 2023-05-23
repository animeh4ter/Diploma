from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=300)
    phone = PhoneNumberField()
    # Try django-address 0.2.8 later
    address = models.CharField(max_length=350)
    profile_img = models.ImageField(upload_to='profiles/', default='profiles/user-default.png')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name
