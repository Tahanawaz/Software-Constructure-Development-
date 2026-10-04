"""Calculation and grading rules for student marks."""


def calculate_total(marks):
    """Return the sum of all marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of all marks."""
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    """Return the letter grade for an average mark."""
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"
