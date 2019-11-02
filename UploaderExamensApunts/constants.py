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
