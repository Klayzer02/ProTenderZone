from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class Subscription(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def is_active(self):
        return self.end_date >= timezone.now()

    def __str__(self):
        return f"Подписка {self.user.username}, активна: {self.is_active()}"

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile', on_delete=models.PROTECT)
    givenName = models.CharField(max_length=100, blank=True, help_text="Введите имя")
    lastName = models.CharField(max_length=100, blank=True)
    patronymicName = models.CharField(max_length=100, blank=True, help_text="Введите отчество")
    mail = models.EmailField(max_length=100, blank=True)
    create_date = models.DateTimeField('Data created', auto_now_add=True)
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.givenName} {self.lastName} {self.patronymicName}"
    def get_full_name(self):
        # Убедитесь, что возвращаются непустые строки
        return f"{self.lastName or 'N/A'} {self.givenName or 'N/A'} {self.patronymicName or 'N/A'}"
    def get_phone_number(self):
        return self.phone
    def get_user(self):
        return self.user
