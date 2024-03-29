from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.db import models
from core import managers as core_managers


class User(AbstractUser):

    """Custom User Model Definition"""

    LOGIN_EMAIL = "email"
    LOGIN_KAKAO = "kakao"
    LOGIN_NAVER = "naver"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_KAKAO, "Kakao"),
        (LOGIN_NAVER, "Naver"),
    )
    avatar = models.ImageField(upload_to="avatar", null=True, blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

    def get_absolute_url2(self):
        return reverse("write-list", kwargs={"pk": self.pk})
