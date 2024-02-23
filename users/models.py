from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)  # Django 기존 유저 모델 상속하기(가져오기)
from django.utils import timezone


# Create your models here.
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        SECRET = ("secret", "Secret")

    first_name = models.CharField(max_length=150, editable=False)  # 성
    last_name = models.CharField(max_length=150, editable=False)  # 이름
    avatar = models.URLField(blank=True)
    name = models.CharField(max_length=150, default="")  # 사용자 이름
    email = models.EmailField(max_length=150)  # 사용자 이메일
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)  # 성별
    created_date = models.DateTimeField(default=timezone.now)  # 계정 만든 시간
    is_active = models.BooleanField(default=True)  # 계정 활성화
    is_staff = models.BooleanField(default=False)  # 스테프 권한
    bio = models.TextField(blank=True)  # 사용자 소개
