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
import os

MEDIA_ROOT_SAVED = '/home/uploader/uploads/' # Absolute path to the media directory.
REL_TMP_DIR = 'tmp'
ABS_TMP_DIR = os.path.join(MEDIA_ROOT_SAVED, REL_TMP_DIR) # Absolute path to the temporal files directory.
REL_FINAL_DIR = 'files'
ABS_FINAL_DIR = os.path.join(MEDIA_ROOT_SAVED, REL_FINAL_DIR)
CONTENT_TYPES = ['application/pdf'] # Accepted formats.
FIRST_YEAR = 2000 # First year to start computing courses.
MAX_FILE_SIZE = 536870912 # Maximum size of the uploaded files in bytes.

# Concurs capsa upload type points
APUNTS_POINTS = 1
EXAMEN_POINTS = 1
RESUM_POINTS = 1
FORMULARI_POINTS = 1
DEFAULT_POINTS = 1
