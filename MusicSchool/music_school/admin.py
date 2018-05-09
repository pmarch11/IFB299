from django.contrib import admin
from .models import UserProfile, bookingsModel, bookingsModelRecurring

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	admin.site.register(UserProfile)

admin.site.register(bookingsModel)
admin.site.register(bookingsModelRecurring)

