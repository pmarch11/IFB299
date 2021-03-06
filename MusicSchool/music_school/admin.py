from django.contrib import admin
from .models import UserProfile, bookingModelInitial, bookingModelDetail, instrumentStockModel, instrumentRequestModel,TeacherProfile, resumeModel, feedbackModel


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	admin.site.register(UserProfile)


class TeacherAdmin(admin.ModelAdmin):
	admin.site.register(TeacherProfile)

#admin.site.register(bookingModelInitial)
admin.site.register(bookingModelDetail)
admin.site.register(instrumentStockModel)
admin.site.register(instrumentRequestModel)
admin.site.register(resumeModel)
admin.site.register(feedbackModel)

class BookingAdmin(admin.ModelAdmin):
	readonly_fields = ('bookingID')

admin.site.register(bookingModelInitial)