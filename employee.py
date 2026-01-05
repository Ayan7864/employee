def get_employee_details(name, emp_id, department, salary):
    """
    Accepts employee details and returns a formatted string.
    """
    formatted_details = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return formatted_details


if __name__ == "__main__":
    # Sample data
    name = "John"
    emp_id = "E001"
    department = "IT"
    salary = 50000

    result = get_employee_details(name, emp_id, department, salary)
    print(result)
