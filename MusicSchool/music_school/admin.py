from django.contrib import admin
from .models import UserProfile, bookingModel, bookingModelRecurring, instrumentStockModel, instrumentRequestModel

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	admin.site.register(UserProfile)

admin.site.register(bookingModel)
admin.site.register(bookingModelRecurring)
admin.site.register(instrumentStockModel)
admin.site.register(instrumentRequestModel)