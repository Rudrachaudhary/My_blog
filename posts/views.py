from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django import forms
from django.views.generic import ListView

# Create your views here.
class CreatePost(LoginRequiredMixin,CreateView):
    login_url = '/admin/login/'
    template_name = 'post_create.html'
    model = Post
    fields = ["title","content","category","tags","featured"]

    success_url = reverse_lazy('create_post')

class ViewPost(LoginRequiredMixin,ListView):
    login_url = '/admin/login'
    template_name = 'view_post.html'
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class UpdatePost(LoginRequiredMixin,UpdateView):
    login_url = '/admin/login/'
    model = Post
    fields = ["title","content","category","tags","featured"]
    template_name = 'post_edit.html'
    success_url = reverse_lazy('view_post')

class DeletePost(LoginRequiredMixin,DeleteView):
    login_url = '/admin/login/'
    template_name = 'post_delete.html'
    model = Post
    fields = ["title","content","category","tags","featured"]
    success_url = reverse_lazy('view_post')
