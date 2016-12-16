from __future__ import unicode_literals
from django.db import models

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

GRADE_CHOICE = (
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
    ('11', 11),
    ('12', 12),
)


class PotentialStu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    phone = models.CharField(max_length=16, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    parent_phone = models.CharField(max_length=16, blank=True)
    parent_email = models.EmailField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    school = models.CharField(max_length=200, blank=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICE, blank=True)
    gpa = models.CharField(max_length=5, blank=True)
    toefl = models.CharField(max_length=3, blank=True)

    def __unicode__(self):
        return self.name


class CounsellingInfo(models.Model):
    id = models.OneToOneField(PotentialStu, on_delete=models.CASCADE, primary_key=True)
    semester = models.CharField(max_length=20)
    apply_grade = models.CharField(max_length=2, choices=GRADE_CHOICE)
    school1 = models.CharField(max_length=100, blank=True)
    school2 = models.CharField(max_length=100, blank=True)
    school3 = models.CharField(max_length=100, blank=True)
    note = models.TextField(blank=True)
    counsellor = models.CharField(max_length=50)
    date = models.DateField()
    status = models.CharField(max_length=10, blank=True)
    fee = models.IntegerField(blank=True)
    pay_date = models.DateField(blank=True)