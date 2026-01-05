from employee import get_employee_details 

def test_get_employee_details():
    name = "John"
    emp_id = "E001"
    department = "IT"
    salary = 50000
   
 expected_output = (
        "Employee Name: John\n"
        "Employee ID: E001\n"
        "Department: IT\n"
        "Salary: 50000"
    )
actual_output = get_employee_details(name, emp_id, department, salary)

 assert actual_output == expected_output