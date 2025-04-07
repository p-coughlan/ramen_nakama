from .models import Review
# This context processor fetches all approved reviews from the database and makes them available in the template context.
def approved_reviews(request):
    reviews = Review.objects.filter(approved=True).order_by('-created_at')
    return {'approved_reviews': reviews}
