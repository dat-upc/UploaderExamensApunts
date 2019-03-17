from django.db import models
import datetime

class Upload(models.Model):
    FIRST_YEAR = 2000
    EMPTY = [
        ("", "---")
    ]
    YEARS = [
        (x, str(x) + "-" + str(x + 1)) for x in range(FIRST_YEAR, datetime.datetime.now().year if (
                datetime.datetime.now().month < 9) else datetime.datetime.now().year + 1)
    ]
    SEMESTER = [
        ("Primavera", "Primavera"),
        ("Tardor", "Tardor"),
    ]
    DOCUMENTS = [
        ("Apunts", "Apunts"),
        ("Examen", "Examen"),
        ("Resum", "Resum"),
        ("Formulari", "Formulari"),
    ]
    PARCIAL_FINAL = [
        ("Parcial", "Parcial"),
        ("Final", "Final"),
    ]
    EXAM_TYPES = [
        ("Problemes", "Problemes"),
        ("Test", "Test"),
        ("Mixt", "Mixt"),
        ("Lab", "Laboratori"),
        ("Reav", "Reavaluació")
    ]


    assignatura = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    alumne = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    any = models.CharField(max_length=1, choices=EMPTY+YEARS)
    quadrimestre = models.CharField(max_length=1, choices=EMPTY+SEMESTER)
    document = models.CharField(max_length=1, choices=EMPTY+DOCUMENTS)
    parcial_final = models.CharField(max_length=1, choices=EMPTY+PARCIAL_FINAL, blank=True, null=True)
    tipus_examen = models.CharField(max_length=1, choices=EMPTY+EXAM_TYPES, blank=True, null=True)

    # TODO
    def __str__(self):
        pass