from django.contrib import admin
from .models import User,Worker,WorkLocation,Scheldue,Client,Reservation
# Register your models here.

admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Client)
admin.site.register(WorkLocation)
admin.site.register(Scheldue)
admin.site.register(Reservation)