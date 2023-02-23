from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    #to make the created field to just show up as readonly field
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)