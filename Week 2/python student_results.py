"""Simple Student Results Processor.

No external libraries imported (pure Python).
Calculates average, assigns grade, displays result, and saves to file.
"""

RESULTS_FILE = "results.txt"


def calculate_average(marks):
    """Marks ka average nikalta hai."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def calculate_grade(average):
    """Average ke mutabiq grade return karta hai."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def save_result(name, grade, file_path=RESULTS_FILE):
    """Student ka name aur grade file mein save (append) karta hai."""
    with open(file_path, "a") as file:
        file.write(f"{name},{grade}\n")


def process_student(name, marks, file_path=RESULTS_FILE):
    """Average aur grade calculate karta hai, display karta hai aur file mein save karta hai."""
    average = calculate_average(marks)
    grade = calculate_grade(average)

    print("\n--- Student Result ---")
    print(f"Student : {name}")
    print(f"Average : {average:.2f}")
    print(f"Grade   : {grade}")

    save_result(name, grade, file_path)
    print(f"Result successfully saved to '{file_path}'.")


if __name__ == "__main__":
    # Example student run
    process_student("Ali", [85, 75, 90])