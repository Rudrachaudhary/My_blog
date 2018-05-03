from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from settings.models import Setting
from categories.models import Category
# Create your views here.
class Home(TemplateView):
    template_name='home.html'

class HomeBlog(ListView):
    context_object_name = 'home_blog'
    template_name='home_blog.html'
    queryset = Setting.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['setting'] = self.queryset
        return context
