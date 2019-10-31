from django.shortcuts import render
from uploader.forms import UploadForm, SignUpForm
from UploaderExamensApunts.constants import *
from .utils.queries import check_dni, get_name

def index(request):
    form = UploadForm()
    return render(request, 'uploader/form.html', {'form': form, 'MAX_FILE_SIZE': MAX_FILE_SIZE//1024//1024,
                                                  "content_types": [i.split('/')[1] for i in CONTENT_TYPES if '/' in i]})

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
