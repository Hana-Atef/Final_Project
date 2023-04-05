from django.db import models

# Create your models here.


# class Relation(models.Model):
#   name = models.CharField(max_length = 25)


class Profile(models.Model):

  # GENDER_CHOICES = (
  #         ('M', 'Male'),
  #         ('F', 'Female'),
  #     )
  username = models.CharField(max_length=15)
  fname = models.CharField(max_length=15)
  lname = models.CharField(max_length=15)
  email = models.EmailField(max_length=15)
  password = models.CharField(max_length=8)
  re_password = models.CharField(max_length=8)
  # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  # relation = models.ForeignKey(Relation,on_delete=models.CASCADE)
  class Meta:
      db_table = 'Profile'

  # def __str__(self):
  #   return self.name


class Patient(models.Model):
  patient_name = models.CharField(max_length=10)
  DoB = models.DateField()

  class Meta:
      db_table = 'Patient'

  # def __str__(self):
  #   return self.name