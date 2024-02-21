from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)  # Django 기존 유저 모델 상속하기(가져오기)


# Create your models here.
# class User(AbstractUser):
#     class GenderChoices(models.TextChoices):
#         MALE = ("male", "Male")
#         FEMALE = ("female", "Female")

#     first_name = models.CharField(max_length=150, editable=False)
#     last_name = models.CharField(max_length=150, editable=False)
#     avatar = models.URLField(blank=True)
#     name = models.CharField(max_length=150, default="")
