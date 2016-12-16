from django.contrib import admin
from .models import HostName, HostFather, HostMother, Contact, Additional
# Register your models here.

admin.site.register(HostName)
admin.site.register(HostFather)
admin.site.register(HostMother)
admin.site.register(Contact)
admin.site.register(Additional)