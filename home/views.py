from django.shortcuts import render
from news.models import News  # Import your News model

def index(request):
    """
    Render the index page and include the latest featured news item.
    """
    # Query to get the latest featured news item, or fallback to the most recent news item if not featured.
    latest_news = News.objects.filter(featured=True).order_by('-published_date')[:1]
    if not latest_news.exists():
        latest_news = News.objects.order_by('-published_date')[:1]
    
    context = {
        'news': latest_news,
        # Add more context variables here if needed.
    }
    return render(request, 'home/index.html', context)