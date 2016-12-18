from django.contrib import admin
from .models import StudentInfo, FatherInfo, MotherInfo, ContactInfo, MultipleChoice
# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(FatherInfo)
admin.site.register(MotherInfo)
admin.site.register(ContactInfo)

admin.site.register(MultipleChoice)