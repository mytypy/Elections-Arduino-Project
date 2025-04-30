from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id_card', 'election', 'choice')
    readonly_fields = ('id_card', 'election', 'choice')

    def has_add_permission(self, request):
        return False  # Запрет на добавление

    def has_change_permission(self, request, obj=None):
        return False  # Запрет на изменение

    def has_delete_permission(self, request, obj=None):
        return False  # Запрет на удаление

    def has_view_permission(self, request, obj=None):
        return True  # Разрешить только просмотр (опционально)