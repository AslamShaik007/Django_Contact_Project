from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete = models.CASCADE, default=None)
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    info = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 50, choices = gender_choices)
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-id']