from django.contrib import admin
from .models import Plant, Watering, Fertilizer, Photo, Profile

admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Fertilizer)
admin.site.register(Photo)
admin.site.register(Profile)
