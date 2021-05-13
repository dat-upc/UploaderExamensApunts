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
from uploader.models import Person, Subject, Degree

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

def list_subjects(degree):
    queryset = [s["nom"] for s in Subject.objects.all().filter(degree__shortName=degree).values("nom")]
    result = ['---'] + list(queryset)
    return result

def get_subject_path(shortName, degree):
    path = Subject.objects.all().filter(shortName=shortName, degree__shortName=degree)[0].path
    return path[path.rfind('/')+1:]

def get_degrees():
    queryset = [d["nom_curt"] for d in Degree.objects.all().values("nom_curt")]
    result = ['---'] + list(queryset)
    return result
