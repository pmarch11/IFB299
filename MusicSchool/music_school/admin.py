from django.contrib import admin
from .models import UserProfile, bookingModel, bookingModelRecurring, instrumentStockModel, instrumentRequestModel,TeacherProfile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	admin.site.register(UserProfile)

class TeacherAdmin(admin.ModelAdmin):
	admin.site.register(TeacherProfile)

admin.site.register(bookingModel)
admin.site.register(bookingModelRecurring)
admin.site.register(instrumentStockModel)
admin.site.register(instrumentRequestModel)