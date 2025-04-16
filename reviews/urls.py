from django.urls import path
from .views import submit_review, review_success, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    # Existing endpoints
    path('submit/', submit_review, name='submit_review'),
    path('review-success/', review_success, name='review_success'),
    # New edit and delete endpoints
    path('edit/<int:pk>/', ReviewUpdateView.as_view(), name='review_edit'),
    path('delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]
