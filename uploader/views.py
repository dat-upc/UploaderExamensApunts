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
from django.shortcuts import render
from uploader.forms import UploadForm, SignUpForm
from UploaderExamensApunts.constants import *
from .utils.queries import check_dni, get_name, list_subjects

def index(request):
    form = UploadForm()
    subjects = {}
    for d in DEGREES.keys():
        subjects[d] = list_subjects(d)
    return render(request, 'uploader/form.html', {'form': form, 'MAX_FILE_SIZE': MAX_FILE_SIZE//1024//1024,
                                                  "content_types": [i.split('/')[1] for i in CONTENT_TYPES if '/' in i],
                                                  "degrees": DEGREES.keys(),
                                                  "subjects": subjects,
                                                  })

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            if not check_dni(form.cleaned_data["dni"]):
                return render(request, 'uploader/error.html', {'error': "El DNI/NIE introduït no està registrat.",
                                                               "error_info": form.errors})
            upload = form.save(commit=False) # Save the form but don't send it to the DB.
            upload.alumne = get_name(upload.dni)
            upload.save() # Now send it to the DB.
            return render(request, 'uploader/success.html') # Say thank you to the uploader.
        else:
            return render(request, 'uploader/error.html', {'error': "Les dades introduïdes no són vàlides.",
                                                           "error_info": form.errors})
    else:
        return render(request, 'uploader/error.html', {'error': "No s'han introduït dades.",
                                                       "error_info": ""})

def signup(request):
    form = SignUpForm()
    return render(request, 'signup/form.html', {'form': form})

def perform_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() # Save the form to the database.
            return render(request, 'signup/success.html') # Say thank you to the uploader.
        else:
            return render(request, 'signup/error.html', {'error': "Les dades introduïdes no són vàlides.",
                                                           "error_info": form.errors})
    else:
        return render(request, 'signup/error.html', {'error': "No s'han introduït dades.",
                                                       "error_info": ""})
