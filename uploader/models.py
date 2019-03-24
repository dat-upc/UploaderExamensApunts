from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from .utils.format_checker import ContentTypeRestrictedFileField
from UploaderExamensApunts.constants import *
from .utils.change_name import change_name
import datetime

class Upload(models.Model):
    MAX_LENGTH = 100
    EMPTY = [
        ("", "---")
    ]
    YEARS = [
        (str(x) + "_" + str((x+1)%100), str(x) + "-" + str(x + 1)) for x in range(FIRST_YEAR, datetime.datetime.now().year if (
                datetime.datetime.now().month < 9) else datetime.datetime.now().year + 1)
    ]
    SEMESTER = [
        ("primavera", "Primavera"),
        ("tardor", "Tardor"),
    ]
    DOCUMENTS = [
        ("apunts", "Apunts"),
        ("examen", "Examen"),
        ("resum", "Resum"),
        ("formulari", "Formulari"),
    ]
    PARCIAL_FINAL = [
        ("parcial", "Parcial"),
        ("final", "Final"),
    ]
    EXAM_TYPES = [
        ("problemes", "Problemes"),
        ("test", "Test"),
        ("mixt", "Mixt"),
        ("laboratori", "Laboratori"),
        ("reavaluacio", "Reavaluació")
    ]

    upload_date = models.DateField(default=timezone.now)
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
    file_upload = ContentTypeRestrictedFileField(upload_to=change_name, content_types=CONTENT_TYPES, max_upload_size=MAX_FILE_SIZE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

# Delete the file when it is deleted from the admin panel.
@receiver(pre_delete, sender=Upload)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.file_upload.delete(False)