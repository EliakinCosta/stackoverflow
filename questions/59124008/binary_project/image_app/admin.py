from django.contrib import admin
from .models import Word
from .forms import ThermalSourceForm


class ThermalSourceAdmin(admin.ModelAdmin):
    form = ThermalSourceForm
    list_display = ('name', 'scheme_image_tag')

# Register your models here.
admin.site.register(Word, ThermalSourceAdmin)
