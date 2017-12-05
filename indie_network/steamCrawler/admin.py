from django.contrib import admin

from .models import Games

class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'photo']
    search_fields = ['name', 'genre']
    fieldsets = [
        ('Games', {'fields': ['name', 'genre', 'photo']}),

    ]
   


# '''

admin.site.register(Games, GameAdmin)
