from uploader.models import Person

def check_dni(dni):
    people = Person.objects.all().filter(dni=dni)
    dni_list = [person.dni for person in people]
    return dni in dni_list