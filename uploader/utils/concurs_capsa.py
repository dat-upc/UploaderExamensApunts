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