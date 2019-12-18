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
from directorySeeker.models import Degree, Subject

# Inserts, removes and updates degrees.
def update_degrees(degreeDict, longNames):
    currentDegrees = [d['shortName'] for d in Degree.objects.values("shortName")]
    for d in currentDegrees:
        if d not in list(degreeDict.keys()):
            Degree.objects.filter(shortName=d).delete()
    for shortName, path in degreeDict.items():
        if shortName in currentDegrees:
            if path != Degree.objects.all().filter(shortName=shortName)[0].path:
                Degree.objects.filter(shortName=shortName).update(path=path)
        else:
            d = Degree(shortName=shortName, path=path, longName=longNames[shortName])
            d.save()

# Inserts, removes and updates subjects.
def update_subjects(subjectDict, degree):
    relatedDegree = Degree.objects.all().filter(shortName=degree)[0]
    currentSubjects = [d['shortName'] for d in Subject.objects.filter(degree=relatedDegree).values("shortName")]
    print (currentSubjects)
    for s in currentSubjects:
        if s not in list(subjectDict.keys()):
            Subject.objects.filter(shortName=s).delete()
    for shortName, path in subjectDict.items():
        path = path[path.rfind('/')+1:]
        if shortName in currentSubjects:
            if path != Subject.objects.all().filter(shortName=shortName)[0].path:
                Subject.objects.filter(shortName=shortName).update(path=path)
        else:
            s = Subject(shortName=shortName, path=path, degree=relatedDegree)
            s.save()
