from django.shortcuts import render
from django.views.generic import ListView
from .models import News

class NewsArchiveView(ListView):
    model = News
    template_name = 'news_archive.html'  # Create this template file
    context_object_name = 'news_list'
    paginate_by = 10  # Optional: Add pagination if desired

