from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms
from django.contrib import auth
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignUP(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ViewUsers(LoginRequiredMixin,ListView):
    login_url = '/admin/login/'
    template_name = 'accounts/users.html'
    model = auth.models.User
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
