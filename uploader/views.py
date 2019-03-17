from django.shortcuts import render
from uploader.forms import UploadForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    form = UploadForm()
    return render(request, 'uploader/form.html', {'form': form})

def upload(request):
    if (request.method == "POST"):
        form = UploadForm(request.POST)
        if (form.is_valid()):
            # It never enters here. Why?
            # Do stuff.
            #return render(request, 'uploader/sucess.html')
            return render(request, 'uploader/success.html')
        return render(request, 'uploader/error.html', {'error': "Les dades introduïdes no són vàlides."})
    else:
        return render(request, 'uploader/error.html', {'error': "No s'han introduït dades."})