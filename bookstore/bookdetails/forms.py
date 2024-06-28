from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['post_title','post_details']

