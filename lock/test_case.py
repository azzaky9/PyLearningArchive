from discount import is_eligible_for_discount

def test_discount_eligibility():
    test_cases = [
        {"age": 16, "student_status": False, "income": 0, "expected": True, "description": "Age < 18"},
        {"age": 20, "student_status": True, "income": 5000, "expected": True, "description": "Age 18-25 and a student"},
        {"age": 22, "student_status": False, "income": 15000, "expected": False,
         "description": "Age 18-25 and not a student"},
        {"age": 30, "student_status": False, "income": 25000, "expected": True,
         "description": "Age > 25 and income < 30000"},
        {"age": 35, "student_status": False, "income": 40000, "expected": False,
         "description": "Age > 25 and income >= 30000"},
        {"age": 25, "student_status": True, "income": 10000, "expected": True, "description": "Age = 25 and a student"},
        {"age": 18, "student_status": False, "income": 10000, "expected": False,
         "description": "Age = 18 and not a student"}
    ]

    for case in test_cases:
        age = case["age"]
        student_status = case["student_status"]
        income = case["income"]
        expected = case["expected"]
        description = case["description"]

        result = is_eligible_for_discount(age, student_status, income)
        assert result == expected, f"Failed: {description} - Expected {expected}, but got {result}"

