from django.shortcuts import render
from uploader.forms import UploadForm

# Create your views here.
def index(request):
    if (request.method == "POST"):
        form = UploadForm(request.POST)
        if (form.is_valid()):
            # Do stuff.
            pass
    else:
        form = UploadForm()

    return render(request, 'uploader/form.html')