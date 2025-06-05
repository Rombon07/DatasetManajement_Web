# dataset/forms.py
from django import forms
from .models import Dataset


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ["name", "description", "cover_image", "data_file"]
