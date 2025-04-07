from django.contrib import admin
from .models import Review

def approve_reviews(modeladmin, request, queryset):
    queryset.update(approved=True)
approve_reviews.short_description = "Approve selected reviews"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'review_text')
    actions = [approve_reviews]
