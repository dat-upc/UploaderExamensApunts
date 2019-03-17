from django.db import models
from .utils.formatChecker import ContentTypeRestrictedFileField
from UploaderExamensApunts.settings import MAX_FILE_SIZE
import datetime

class Upload(models.Model):
    FIRST_YEAR = 2000
    MAX_LENGTH = 100
    EMPTY = [
        ("", "---")
    ]
    YEARS = [
        (str(x), str(x) + "-" + str(x + 1)) for x in range(FIRST_YEAR, datetime.datetime.now().year if (
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

    upload_date = models.DateField(default=datetime.datetime.today().strftime('%Y-%m-%d'))
    assignatura = models.CharField(max_length=MAX_LENGTH)
    professor = models.CharField(max_length=MAX_LENGTH)
    alumne = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH)
    curs = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+YEARS)
    quadrimestre = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+SEMESTER)
    document = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+DOCUMENTS)
    parcial_final = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+PARCIAL_FINAL, blank=True, null=True)
    tipus_examen = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+EXAM_TYPES, blank=True, null=True)
    solucio = models.BooleanField(default=False)
    file_upload = ContentTypeRestrictedFileField(upload_to="tmp", content_types=['application/pdf'], max_upload_size=MAX_FILE_SIZE, null=True, blank=True)