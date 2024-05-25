from django.contrib import admin
from enroll.models import *
# Register your models here.
admin.site.register(newuser)
admin.site.register(Stationowner)
admin.site.register(Stations)
admin.site.register(Bookslots)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(DeletedBooking)