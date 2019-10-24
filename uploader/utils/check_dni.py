from uploader.models import Person

def check_dni(dni):
    people = Person.objects.all().filter(dni=dni) # List size should be 1
    dni_list = [person.dni for person in people]
    return dni in dni_list