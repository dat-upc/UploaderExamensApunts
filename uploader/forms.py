from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        exclude = ()

# Check why JQuery isn't loaded properly using this form generator.
# Add file upload.