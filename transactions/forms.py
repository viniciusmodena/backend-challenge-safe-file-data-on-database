from django import forms  
from django.core.validators import FileExtensionValidator

class FileForm(forms.Form):  
    file = forms.FileField(validators=[FileExtensionValidator( ['txt'], message="Your file must be a txt file" ) ]) 
