"""Run the Student Marks application."""

from calculations import calculate_average, calculate_grade, calculate_total
from display import display_result
from validation import validate_mark


def main():
    """Collect input and coordinate validation, calculation, and display."""
    name = input("Enter the student's name: ")
    marks = []

    # Collect exactly three valid subject marks.
    for subject_number in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {subject_number}: "))
            except ValueError:
                print("Invalid marks. Enter 0-100.")
                continue

            if validate_mark(mark):
                marks.append(mark)
                break

            print("Invalid marks. Enter 0-100.")

    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)


if __name__ == "__main__":
    main()
