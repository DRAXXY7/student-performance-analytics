def calculate_total(python, mathematics, statistics):
    total = python + mathematics + statistics
    return total


def calculate_average(total):
    average = total / 3
    return average


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(python, mathematics, statistics):
    if python >= 40 and mathematics >= 40 and statistics >= 40:
        return "Pass"
    else:
        return "Fail"