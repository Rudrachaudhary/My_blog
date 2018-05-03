from django.shortcuts import render
from .models import Setting
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView

# Create your views here.
class UpdateSetting(LoginRequiredMixin,UpdateView):
    login_url = '/admin/login/'
    model = Setting
    fields = ["site_name","contact_number","contact_email","address"]
    template_name = 'edit_setting.html'
    success_url = reverse_lazy('view_setting')

class ViewSetting(LoginRequiredMixin,ListView):
    login_url = '/admin/login'
    template_name = 'view_setting.html'
    model = Setting
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateSetting(LoginRequiredMixin,CreateView):
    login_url = '/admin/login/'
    template_name = 'create_setting.html'
    model = Setting
    fields = ["site_name","contact_number","contact_email","address"]

    success_url = reverse_lazy('view_setting')

class DeleteSetting(LoginRequiredMixin,DeleteView):
    login_url = '/admin/login/'
    template_name = 'delete_setting.html'
    model = Setting
    fields = ["site_name","contact_number","contact_email","address"]
    success_url = reverse_lazy('view_setting')
