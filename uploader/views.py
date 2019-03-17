from django.shortcuts import render
from uploader.forms import UploadForm
from UploaderExamensApunts.settings import MAX_FILE_SIZE

def index(request):
    form = UploadForm()
    return render(request, 'uploader/form.html', {'form': form, 'MAX_FILE_SIZE': MAX_FILE_SIZE//1024//1024})

def upload(request):
    if (request.method == "POST"):
        form = UploadForm(request.POST, request.FILES)
        print (form.errors) # Display the form errors for debugging purposes.
        if (form.is_valid()):
            form.save() # Save the form to the database.
            return render(request, 'uploader/success.html') # Say thank you to the uploader.
        else:
            return render(request, 'uploader/error.html', {'error': "Les dades introduïdes no són vàlides.",
                                                           "error_info": form.errors})
    else:
        return render(request, 'uploader/error.html', {'error': "No s'han introduït dades.",
                                                       "error_info": ""})