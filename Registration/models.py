from django.db import models

# Create your models here.

class Profile(models.Model):
  username = models.CharField(max_length=15)
  fname = models.CharField(max_length=15)
  lname = models.CharField(max_length=15)
  email = models.EmailField(max_length=15)
  password = models.CharField(max_length=8)
  re_password = models.CharField(max_length=8)

  class Meta:
      db_table = 'Profile'

  # def __str__(self):
  #   return self.name