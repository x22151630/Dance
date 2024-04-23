from django.contrib import admin

# Register your models here.


from .models import Dance,Events
admin.site.register(Dance)
admin.site.register(Events)