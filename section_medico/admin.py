from django.contrib import admin

# Register your models here.
from .models import Prenotazioni, News, ApiKeys

admin.site.register(Prenotazioni)
admin.site.register(News)
admin.site.register(ApiKeys)
