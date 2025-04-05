from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'review_text')


