# Copyright (C) 2019 Aniol Marti
# This file is part of DAT - UploaderExamensApunts.
#
# DAT - UploaderExamensApunts is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DAT - UploaderExamensApunts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with DAT - UploaderExamensApunts. If not, see <https://www.gnu.org/licenses/>.
#
from django.db import models
from django.utils import timezone
from .utils.format_checker import ContentTypeRestrictedFileField
from .utils.change_name import change_name
from UploaderExamensApunts.constants import *
import datetime

class Person(models.Model):
    # Django autocompletes plural names and writes "Persons" instead of "People".
    class Meta:
        verbose_name_plural = "people"
    MAX_LENGTH = 100

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=MAX_LENGTH)
    email = models.EmailField(max_length=MAX_LENGTH, unique=True)
    dni = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name="DNI/NIE")
    punts_capsa = models.PositiveIntegerField(default=0)

class Upload(models.Model):
    MAX_LENGTH = 100
    EMPTY = [
        ("", "---")
    ]
    YEARS = [
        (str(x) + "_" + str((x+1)%100), str(x) + "-" + str(x + 1)) for x in range(FIRST_YEAR, datetime.datetime.now().year if (
                datetime.datetime.now().month < 9) else datetime.datetime.now().year + 1)
    ]
    DEGREES = [
        ("GR15", "Grau en Enginyeria de Tecnologies i Serveis de Telecomunicació"),
        ("GREE", "Grau en Enginyeria Electrònica de Telecomunicació"),
        ("GREF", "Grau en Enginyeria Física"),
        ("GRCED", "Grau en Ciència i Enginyeria de Dades"),
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
        ("reavaluacio", "Reavaluació"),
    ]

    id = models.AutoField(primary_key=True)
    upload_date = models.DateField(default=timezone.now)
    grau = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+DEGREES)
    assignatura = models.CharField(max_length=MAX_LENGTH)
    professor = models.CharField(max_length=MAX_LENGTH)
    dni = models.CharField(max_length=MAX_LENGTH)
    alumne = models.CharField(max_length=MAX_LENGTH, blank=True, default="")
    curs = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+YEARS)
    quadrimestre = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+SEMESTER)
    document = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+DOCUMENTS)
    parcial_final = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+PARCIAL_FINAL, blank=True, null=True)
    tipus_examen = models.CharField(max_length=MAX_LENGTH, choices=EMPTY+EXAM_TYPES, blank=True, null=True)
    solucio = models.BooleanField(default=False)
    file_upload = ContentTypeRestrictedFileField(upload_to=change_name, content_types=CONTENT_TYPES, max_upload_size=MAX_FILE_SIZE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
