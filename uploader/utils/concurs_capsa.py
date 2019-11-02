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
from .queries import get_points, update_points

def add_points(upload_type, dni):
    points = get_points(dni)

    if upload_type == "apunts":
        points += APUNTS_POINTS
    elif upload_type == "examen":
        points += EXAMEN_POINTS
    elif upload_type == "resum":
        points += RESUM_POINTS
    elif upload_type == "formulari":
        points += FORMULARI_POINTS
    else:
        points += DEFAULT_POINTS

    update_points(dni, points)