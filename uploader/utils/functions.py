import datetime

def get_courses(first_year):
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year if (month < 9) else datetime.datetime.now().year + 1
    courses = []
    i = first_year
    while (i < year):
        courses.append(str(i) + "-" + str(i + 1))
        i += 1
    return courses