from django.shortcuts import render
from .utils.functions import *

# Create your views here.
def index(request):
    first_year = 2000
    courses = get_courses(first_year)
    return render(request, "uploader/form.html", {"courses": courses, "first_year": first_year})