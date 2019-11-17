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
from django.db import models

class Degree(models.Model):
    MAX_LENGTH = 100

    id = models.AutoField(primary_key=True)
    shortName = models.CharField(max_length=MAX_LENGTH, unique=True)
    longName = models.EmailField(max_length=MAX_LENGTH)

class Subject(models.Model):
    MAX_LENGTH = 100

    id = models.AutoField(primary_key=True)
    shortName = models.CharField(max_length=MAX_LENGTH, unique=True)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
