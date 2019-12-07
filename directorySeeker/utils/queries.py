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

## WIP ##

# Inserts, removes and updates degrees.
def update_degrees(degreeDict, path, longName):
    currentDegrees = list(Degree.objects.values("shortName", flat=True))
    for d in currentDegrees:
        if d not in degreeDict.keys():
            Degree.objects.filter(shortName=d).delete()
    for shortName, path in degreeDict.items():
        if shortName in currentDegrees:
            if path != Degree.objects.all.filter(shortName=shortName)[0].path
                Degree.objects.filter(shortName=shortName).update(path=path)
        else:
            d = Degree(shortName=shortName, path=path, longName=longName)
            d.save()

# Inserts, removes and updates subjects.
def update_subjects(subjectDict, path):
    pass
