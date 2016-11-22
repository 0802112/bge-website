from __future__ import unicode_literals
from django.db import models


class PotentialStu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    agent = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    school = models.CharField(max_length=200)
    grade = models.CharField(max_length=2)
    gpa = models.FloatField()
    toefl = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name


class CounsellingInfo(models.Model):
    id = models.ForeignKey(PotentialStu, on_delete=models.CASCADE, primary_key=True)
    semester = models.CharField(max_length=20)
    apply_grade = models.IntegerField()
    school1 = models.CharField(max_length=50)
    school2 = models.CharField(max_length=50)
    school3 = models.CharField(max_length=50)
    note = models.CharField(max_length=200)
    counsellor = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    fee = models.IntegerField()
    pay_date = models.CharField(max_length=50)