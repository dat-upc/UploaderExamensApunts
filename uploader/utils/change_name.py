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
from UploaderExamensApunts.constants import *

def change_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    data = str(instance.upload_date.strftime("%d_%m"))
    if instance.document == "examen":
        name = instance.assignatura + "-y." + instance.curs + "-" + instance.document + "_" + \
               instance.parcial_final + "_" + instance.tipus_examen + "-q." + instance.quadrimestre\
               + "-d." + data + "-p." + instance.professor.replace(" ", "_") + "-a." + \
               instance.alumne.replace(" ", "_")
        if instance.solucio:
            name = name + "-s"
        name = name + extension
    else:
        name = instance.assignatura.nom + "-y." + instance.curs + "-" + instance.document.nom + "-q." + \
               instance.quadrimestre + "-d." + data + "-p." + instance.professor.replace(" ", "_") + "-a." + \
               instance.alumne.replace(" ", "_") + extension
    return os.path.join(REL_TMP_DIR, name)
