from django.contrib import admin
from .models import ChoiceModel


@admin.register(ChoiceModel)
class ChoiceAdmin(admin.ModelAdmin):
    pass
