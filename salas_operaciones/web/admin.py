from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Mascota)
admin.site.register(Sala)
admin.site.register(Procedimiento)