from django.shortcuts import render
from .utils.functions import *
from .utils.forms import UploadForm

# Create your views here.
def index(request):
    #first_year = 2000
    #courses = get_courses(first_year)
    #return render(request, "uploader/form_basic.html", {"courses": courses, "first_year": first_year})
    form = UploadForm()
    return render(request, 'uploader/form.html', {'form': form})

def upload(request):
    if (request.method == "POST"):
        form = UploadForm(request.POST)
        if (form.is_valid()):
            # Do stuff.
            pass
    else:
        form = UploadForm()

    return render(request, 'uploader/form.html') # This should change.