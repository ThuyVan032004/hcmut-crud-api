from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Person)
admin.site.register(EmailAddress)
admin.site.register(BusinessEntity)
admin.site.register(Address)
admin.site.register(StateProvince)
admin.site.register(AddressType)
admin.site.register(BusinessEntityAddress)
admin.site.register(CountryRegion)



