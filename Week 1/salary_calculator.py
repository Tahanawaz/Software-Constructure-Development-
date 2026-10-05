"""Simple Employee Salary Calculator.

No external libraries imported (pure Python).
Calculates Gross and Net salary based on user inputs.
"""


def calculate_gross_salary(basic_salary, allowances=0.0, bonus=0.0):
    """Gross salary = basic salary + allowances + bonus."""
    return basic_salary + allowances + bonus


def calculate_net_salary(gross_salary, deductions=0.0):
    """Net salary = gross salary - deductions."""
    return gross_salary - deductions


def get_positive_number(prompt):
    """User se positive number lene ka simple function."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Amount cannot be negative. Please enter 0 or more.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def display_salary_summary(employee_name, gross_salary, deductions, net_salary):
    """Salary ka final summary display karta hai."""
    print("\n--- Monthly Salary Summary ---")
    print(f"Employee Name : {employee_name}")
    print(f"Gross Salary  : {gross_salary:.2f}")
    print(f"Deductions    : {deductions:.2f}")
    print(f"Net Salary    : {net_salary:.2f}")


def main():
    print("=== Employee Salary Calculator ===")

    employee_name = input("Enter employee name: ").strip()
    while not employee_name:
        print("Employee name cannot be empty.")
        employee_name = input("Enter employee name: ").strip()

    basic_salary = get_positive_number("Enter basic salary: ")
    allowances = get_positive_number("Enter allowances (0 if none): ")
    bonus = get_positive_number("Enter bonus (0 if none): ")

    gross_salary = calculate_gross_salary(basic_salary, allowances, bonus)

    while True:
        deductions = get_positive_number("Enter deductions (0 if none): ")
        if deductions <= gross_salary:
            break
        print(f"Deductions cannot exceed gross salary ({gross_salary:.2f}). Try again.")

    net_salary = calculate_net_salary(gross_salary, deductions)

    display_salary_summary(employee_name, gross_salary, deductions, net_salary)


if __name__ == "__main__":
    main()
