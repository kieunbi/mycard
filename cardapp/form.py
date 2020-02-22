from django.db import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Mate:
        Model = Blog
        fields = ['title','body']