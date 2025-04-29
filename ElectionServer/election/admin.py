from django.contrib import admin
from .models import ElectionModel
from choice.models import ChoiceModel


class ChoiceInline(admin.TabularInline):
    model = ChoiceModel
    extra = 1


@admin.register(ElectionModel)
class ElectionVotingAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created')
    inlines = [
        ChoiceInline
        ]
