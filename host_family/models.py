from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

MARITAL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
)

GENDER_CHOICE = (
    ('m', 'M'),
    ('f', 'F'),
)


class HostName(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class HostFather(models.Model):
    id = models.OneToOneField(HostName, on_delete=models.CASCADE, primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    marital = models.CharField(max_length=8, choices=MARITAL_STATUS)
    occupation = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __unicode__(self):
        return self.lastname

    def get_absolute_url(self):
        return reverse('host_edit', kwargs={'pk': self.pk})


class HostMother(models.Model):
    id = models.OneToOneField(HostName, on_delete=models.CASCADE, primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    marital = models.CharField(max_length=8, choices=MARITAL_STATUS)
    occupation = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __unicode__(self):
        return self.lastname

    def get_absolute_url(self):
        return reverse('host_edit', kwargs={'pk': self.pk})


class Contact(models.Model):
    id = models.OneToOneField(HostName, on_delete=models.CASCADE, primary_key=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=15)
    type = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    cellular = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    email = models.EmailField()


class Additional(models.Model):
    id = models.OneToOneField(HostName, on_delete=models.CASCADE, primary_key=True)
    name1 = models.CharField(max_length=100)
    gender1 = models.CharField(max_length=2, choices=GENDER_CHOICE)
    relation1 = models.CharField(max_length=50)
    school1 = models.CharField(max_length=100)
    age1 = models.CharField(max_length=3)
    grade1 = models.CharField(max_length=100)

    name2 = models.CharField(max_length=100)
    gender2 = models.CharField(max_length=2, choices=GENDER_CHOICE)
    relation2 = models.CharField(max_length=50)
    school2 = models.CharField(max_length=100)
    age2 = models.CharField(max_length=3)
    grade2 = models.CharField(max_length=100)

    name3 = models.CharField(max_length=100)
    gender3 = models.CharField(max_length=2, choices=GENDER_CHOICE)
    relation3 = models.CharField(max_length=50)
    school3 = models.CharField(max_length=100)
    age3 = models.CharField(max_length=3)
    grade3 = models.CharField(max_length=100)

    name4 = models.CharField(max_length=100)
    gender4 = models.CharField(max_length=2, choices=GENDER_CHOICE)
    relation4 = models.CharField(max_length=50)
    school4 = models.CharField(max_length=100)
    age4 = models.CharField(max_length=3)
    grade4 = models.CharField(max_length=100)





























