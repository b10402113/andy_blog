from django.contrib import admin

# Register your models here.
from . import models


class EntryAdmin(admin.ModelAdmin):
    list_display = ['entry_title','entry_author','entry_visiting','created_time','isFeatured']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Entry,EntryAdmin)