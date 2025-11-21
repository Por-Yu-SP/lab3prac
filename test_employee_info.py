import employee_info as emp
def test_calculate_average():
    result=emp.calculate_average_salary
    assert(result==361000/6)

def test_get_employees_by_dept():
    result=emp.get_employees_by_dept("Sales")
    expect=[
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    assert(result==expect)

def test_get_employee_by_age_range():
    result=emp.get_employees_by_age_range("22","26")
    expect=[
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    assert(expect==result)


