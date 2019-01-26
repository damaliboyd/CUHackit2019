from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.urls import reverse_lazy

# Create your models here.
class Profile(models.Model):
	user = AutoOneToOneField(User, on_delete="CASCADE")
	first_name = models.TextField()
	last_name = models.TextField()
	major = models.TextField()
	interest = models.TextField()

class CollegeConnect(models.Model):
	profile = models.ForeignKey(to = Profile, on_delete="CASCADE")
