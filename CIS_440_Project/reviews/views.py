from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView, 
    TemplateView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView)
from .models import Review
# from .forms import ReviewForm


# Create your views here.
class ReviewCreateView(LoginRequiredMixin, CreateView):
    # will look for HTML file called review_form.html
    model = Review
    fields = ['review_text', 'would_you_reccommend_our_restaraunt']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = 'reviews/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/list_view.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reviews'
    ordering = ['date_posted']
    paginate_by = 5


class UserReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name = 'reviews/user_reviews.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reviews'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(user=user).order_by('-date_posted')


class ReviewDetailView(DetailView):
    model = Review