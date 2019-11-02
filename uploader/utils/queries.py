from uploader.models import Person

def check_dni(dni):
    people = Person.objects.all().filter(dni=dni) # List size should be 1
    dni_list = [person.dni for person in people]
    return dni in dni_list

def get_name(dni):
    people = Person.objects.all().filter(dni=dni) # List size should be 1
    name_list = [person.nom for person in people]
    return name_list[0]

def get_points(dni):
    return Person.objects.all().filter(dni=dni)[0].punts_capsa

def update_points(dni, points):
    Person.objects.filter(dni=dni).update(punts_capsa=points)
