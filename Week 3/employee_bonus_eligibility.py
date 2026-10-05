def get_employee_details():
    print("--- Enter Employee Details ---")
    name = input("Employee Name: ")
    basic_salary = float(input("Basic salary: "))
    allowance = float(input("Allowance: "))
    tax_rate = float(input("Tax rate (%): "))
    
    is_active = input("Is active employee? (y/n): ").strip().lower() == 'y'
    months_employed = int(input("Months employed: "))
    performance_rating = float(input("Performance rating (1-5): "))
    has_disciplinary_action = input("Has disciplinary action? (y/n): ").strip().lower() == 'y'
    attendance_percentage = float(input("Attendance percentage: "))
    
    return (
        name, 
        basic_salary, 
        allowance, 
        tax_rate, 
        is_active, 
        months_employed, 
        performance_rating, 
        has_disciplinary_action, attendance_percentage)


def check_bonus_eligibility(is_active, months_employed, performance_rating, has_disciplinary_action, attendance_percentage):
    eligible = True
    if not is_active:
        eligible = False
    if months_employed < 12:
        eligible = False
    if performance_rating < 4:
        eligible = False
    if has_disciplinary_action:
        eligible = False
    if attendance_percentage < 90:
        eligible = False

    return eligible


def calculate_bonus_amount(is_eligible):
    return 5000.0 if is_eligible else 0.0


def calculate_gross_salary(basic_salary, allowance, bonus_amount):
    return basic_salary + allowance + bonus_amount


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * (tax_rate / 100)


def calculate_net_salary(gross_salary, tax_amount):
    return gross_salary - tax_amount


def display_salary_slip(name, gross, tax, net, is_eligible, bonus):
    print("\n----- Salary Slip -----")
    print("Employee Name  :", name)
    print("Bonus Eligible :", "Yes" if is_eligible else "No")
    print("Bonus Amount   :", bonus)
    print("Gross Salary   :", gross)
    print("Tax Deducted   :", tax)
    print("Net Salary     :", net)


(name, basic_salary, allowance, tax_rate, is_active, months_employed, performance_rating, has_disciplinary_action, attendance_percentage) = get_employee_details()

is_eligible = check_bonus_eligibility(is_active, months_employed, performance_rating, has_disciplinary_action, attendance_percentage)
bonus_amount = calculate_bonus_amount(is_eligible)

gross = calculate_gross_salary(basic_salary, allowance, bonus_amount)
tax = calculate_tax(gross, tax_rate)
net = calculate_net_salary(gross, tax)

display_salary_slip(name, gross, tax, net, is_eligible, bonus_amount)