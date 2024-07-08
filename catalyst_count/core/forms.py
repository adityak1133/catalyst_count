from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

class FilterForm(forms.Form):
    filter_field = forms.CharField(max_length=100)