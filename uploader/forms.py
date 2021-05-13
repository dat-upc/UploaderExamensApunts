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
from django import forms
from .models import Upload, Person
from captcha.fields import CaptchaField
from UploaderExamensApunts.constants import *
from .utils.queries import get_degrees

class UploadForm(forms.ModelForm):
    captcha = CaptchaField()
    degrees = get_degrees()
    for d in degrees:
        exec("assig" + d + " = forms.CharField()")

    class Meta:
        model = Upload
        fields = ["grau", "assignatura", "professor", "dni", "curs", "quadrimestre", "document", "parcial_final",
                  "tipus_examen", "solucio", "file_upload", "captcha", "alumne"] + ["assig" + d for d in degrees]


class SignUpForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Person
        fields = ["nom", "email", "dni", "captcha"]
