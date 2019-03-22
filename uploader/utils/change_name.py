import os
from UploaderExamensApunts.constants import *

def change_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    data = str(instance.upload_date.strftime("%d_%m"))
    if (instance.document == "examen"):
        name = instance.assignatura + "-y." + instance.curs + "-" + instance.document + "_" + \
               instance.parcial_final + "_" + instance.tipus_examen + "-q." + instance.quadrimestre\
               + "-d." + data + "-p." + instance.professor.replace(" ", "_") + "-a." + \
               instance.alumne.replace(" ", "_")
        if (instance.solucio):
            name = name + "-s"
        name = name + extension
    else:
        name = instance.assignatura + "-y." + instance.curs + "-" + instance.document + "-q." + \
               instance.quadrimestre + "-d." + data + "-p." + instance.professor.replace(" ", "_") + "-a." + \
               instance.alumne.replace(" ", "_") + extension
    return os.path.join(REL_TMP_DIR, name)