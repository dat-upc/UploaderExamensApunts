from django import forms
from .models import Upload, Person
from captcha.fields import CaptchaField

class UploadForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Upload
        fields = ["grau", "assignatura", "professor", "dni", "curs", "quadrimestre", "document", "parcial_final", "tipus_examen", "solucio", "file_upload", "captcha"]

class SignUpForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Person
        fields = ["nom", "email", "dni", "captcha"]
