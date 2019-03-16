from django import forms
import datetime

class UploadForm(forms.Form):
    assignatura = forms.CharField(label="Assignatura", max_length=100)
    professor = forms.CharField(label="Professor", max_length=100)
    alumne = forms.CharField(label="Alumne", max_length=100)
    email = forms.EmailField(label="Correu-e", max_length=100)
    any = forms.ChoiceField(choices=[("", "---")] + [(x, str(x) + "-" + str(x+1))
                                                     for x in range(2000, datetime.datetime.now().year if (datetime.datetime.now().month < 9) else datetime.datetime.now().year + 1)])
    quadrimestre = forms.ChoiceField(choices=[("", "---"), ("Primavera", "Primavera"), ("Tardor", "Tardor")])
    document = forms.ChoiceField(choices=[("", "---"), ("Apunts", "Apunts"), ("Examen", "Examen"), ("Resum", "Resum"), ("Formulari", "Formulari"),])
    parcial_final = forms.ChoiceField(choices=[("", "---"), ("Parcial", "Parcial"), ("Final", "Final")])
    tipus_examen = forms.ChoiceField(choices=[("", "---"), ("Problemes", "Problemes"), ("Test", "Test"), ("Mixt", "Mixt"), ("Lab", "Laboratori"), ("Reav", "Reavaluació")])

    # Check why JQuery isn't loaded properly using this form generator.
    # May be load it from models.py directly aka database.