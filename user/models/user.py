from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER = (("female", "Female"), ("male", "Male"))

    gender = models.CharField(max_length=100, choices=GENDER, verbose_name=_("gender"))
    phone_number = models.CharField(
        max_length=50, blank=True, verbose_name=_("phone number")
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
