from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField

from utils.validators import file_extension_validator


class Analysis(models.Model):
    log_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    section = models.CharField(max_length=1)
    description = models.TextField()  # ArrayField(models.TextField())
    log_file = models.FileField(validators=[file_extension_validator])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
