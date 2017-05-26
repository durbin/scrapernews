from django.contrib import admin
from hackernews import models

class ItemAdmin(admin.ModelAdmin):
    list_display = ('hnid', 'title', 'url', 'hacker', 'points')
    search_fields = ('title', 'url', 'hacker')

admin.site.register(models.Item, ItemAdmin)