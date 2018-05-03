from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        def __init__(self, *args, **kwargs):
            super(CategoryForm, self).__init__(*args, **kwargs)
            self.fields['name'].widget = TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'myCustomPlaceholder'})
