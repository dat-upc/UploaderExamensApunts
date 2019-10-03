from django import forms
from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ["grau", "assignatura", "professor", "alumne", "dni", "email", "curs", "quadrimestre", "document", "parcial_final", "tipus_examen", "solucio", "file_upload"]