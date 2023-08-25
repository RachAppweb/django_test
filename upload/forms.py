from django import forms 
from .models import *


class UploadFileForm(forms.Form):
    
    file =forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))


class editfilecontent(forms.ModelForm):
    class Meta:
        model=original
        fields='__all__'