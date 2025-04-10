# news/urls.py
from django.urls import path
from .views import NewsArchiveView

# This URL pattern will route the root URL of the news app to the NewsArchiveView.
urlpatterns = [
    path('', NewsArchiveView.as_view(), name='news-archive'),
]
