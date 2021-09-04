from django import forms
from . models import Blog

class Edit_BLog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','dsc')