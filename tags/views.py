from django.shortcuts import render
from .models import Tag
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django import forms
from django.views.generic import ListView

# Create your views here.
class ViewTag(LoginRequiredMixin,ListView):
    login_url = '/admin/login/'
    template_name = 'tag_index.html'
    model = Tag
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateTag(LoginRequiredMixin,CreateView):
    login_url = '/admin/login/'
    template_name = 'tag_create.html'
    model = Tag
    fields = ["tag"]
    success_url = reverse_lazy('create_tag')

class DeleteTag(LoginRequiredMixin,DeleteView):
    login_url = '/admin/login/'
    template_name = 'tag_delete.html'
    model = Tag
    fields = ["tag"]
    success_url = reverse_lazy('view_tag')

class UpdateTag(LoginRequiredMixin,UpdateView):
    login_url = '/admin/login/'
    model = Tag
    fields = ['tag']
    template_name = 'tag_edit.html'
    success_url = reverse_lazy('view_tag')
