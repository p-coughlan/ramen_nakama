from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ReviewForm

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()  # review.approved remains False until an admin approves it
            # Use the underscore version here:
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

@login_required
def review_success(request):
    """Render a thank-you page after a review is submitted."""
    return render(request, 'reviews/review_success.html')
