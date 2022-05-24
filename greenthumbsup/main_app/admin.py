from django.contrib import admin
from .models import Plant, Profile, Fertilizer, Photo, Watering

# Register your models here.
admin.site.register(Plant)
admin.site.register(Profile)
admin.site.register(Fertilizer)
admin.site.register(Photo)
admin.site.register(Watering)