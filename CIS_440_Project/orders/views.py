from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Order
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
# Create your views here.


class OrderCreateView(LoginRequiredMixin, CreateView):
    # will look for HTML file called order_form.html
    model = Order
    fields = ['items']
    def get_success_url(self, **kwargs):
        return reverse_lazy('order-detail', args = (self.object.user, self.object.id))


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrderDetailView(DetailView):
    model = Order

    def get_queryset(self):
        queryset = super(DetailView, self).get_queryset()
        return queryset.filter(user=self.request.user)


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''uses generic UpdateView to update Order. Login is required to use. form_valid and test_func validate the current user and form submission'''
    model = Order
    fields = ['items']

    def get_success_url(self, **kwargs):
        return reverse_lazy('order-detail', args = (self.object.user, self.object.id))


    # validates form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    def test_func(self):
        food = self.get_object()
        if self.request.user == food.user:
            return True
        else:
            return False