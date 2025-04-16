from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ReviewForm
from .models import Review

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()  # review.approved remains False until an admin approves it
            return redirect('review_success')
    else:
        form = ReviewForm()
    return render(request, 'reviews/submit_review.html', {'form': form})

@login_required
def review_success(request):
    """
    Render a thank-you page after a review is submitted.
    """
    return render(request, 'reviews/review_success.html')

class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit_review.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # Mark edited reviews unapproved until re-approved by admin
        form.instance.approved = False
        return super().form_valid(form)

    def test_func(self):
        # Ensure only the review's author can edit
        return self.request.user == self.get_object().user

class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = 'reviews/confirm_delete_review.html'
    success_url = reverse_lazy('profile')

    def test_func(self):
        # Ensure only the review's author can delete
        return self.request.user == self.get_object().user
