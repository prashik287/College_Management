import random
import datetime

def stdgen(department):
    """
    Generate a student id  for specified department
    """
    s= ""
    if department == "Information Technology":
        s = "IT"
    elif department == "Computer Science ":
        s = "CS"
    elif department == "Cybersecurity":
        s = "CY"
    elif department == "Mechanical":
        s = "ME"
    elif department == "Civil":
        s = "CI"
    elif department == "Chemical":
        s = "CL"

    current_year = datetime.date.today().year
    # print(current_year)
    random_number = random.randint(1, 100)
    random_number_str = str(random_number)
    if len(random_number_str) < 3:
        random_number_str = '0' * (3 - len(random_number_str)) + random_number_str
    stdid = str(current_year) + s + random_number_str
    print(stdid)
    return stdid
    # print(random_number_str)

# stdgen("Information Technology")