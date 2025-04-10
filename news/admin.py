from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'featured')
    list_filter = ('featured', 'published_date')
    search_fields = ('title', 'content')

