from django.shortcuts import render
from .models import Category
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import CategoryForm
from django.forms import modelform_factory
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class CreateCategory(LoginRequiredMixin,CreateView):
    login_url = '/admin/login/'
    template_name = 'category_create.html'
    model = Category
    fields = ["name"]
    success_url = reverse_lazy('create_category')
    success_message = "%(name)s was created successfully"
    def get_form_class(self):
          return modelform_factory(self.model, form=CategoryForm, fields=self.fields)

class DeleteCategory(LoginRequiredMixin,DeleteView):
    login_url = '/admin/login/'
    template_name = 'category_delete.html'
    model = Category
    fields = ["name"]
    success_url = reverse_lazy('view_categories')
    success_message = "%(name)s was deleted successfully"

class UpdateCategory(LoginRequiredMixin,UpdateView):
    login_url = '/admin/login/'
    model = Category
    fields = ['name']
    template_name = 'category_edit.html'
    success_url = reverse_lazy('view_categories')

class ViewCategories(LoginRequiredMixin,ListView):
    login_url = '/admin/login/'
    template_name = 'category_index.html'
    model = Category
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
