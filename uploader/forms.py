from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["assignatura", "professor", "alumne", "email", "any", "quadrimestre", "document", "parcial_final", "tipus_examen"]

# Check why JQuery isn't loaded properly using this form generator.
# Add file upload.