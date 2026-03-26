users = [
    {"id": 1, "name": "John", "salary": 500},
    {"id": 2, "name": "", "salary": 300},
    {"id": 3, "name": "Anna", "salary": -100},
    {"id": None, "name": "Mike", "salary": 400}
]


def validate_id(user_id):
    """
    Checks if the user s Id is None.
    Returns an error message string if None, otherwise returns None.
    """
    return "id is None" if user_id is None else None


def validate_name(name):
    """
    Checks if the user's name is empty.
    Returns an error message string if empty, otherwise returns None.
    """
    return "name is empty" if not name else None


def validate_salary(salary):
    """
    Checks if the user's salary is positive.
    Returns an error message string if not positive, otherwise returns None.
    """
    return "salary is not positive" if salary <= 0 else None


def validate_user(user):
    """
    Calls all validation functions for a single user.
    Returns a list of reasons why the user is invalid.
    """
    reasons = list(filter(None, [
        validate_id(user.get("id")),
        validate_name(user.get("name")),
        validate_salary(user.get("salary", 0))
    ]))
    return reasons



invalid_records = []

for user in users:
    reasons = validate_user(user)
    if reasons:  
        invalid_records.append({
            "name": user.get("name"),
            "reasons": reasons
        })


for record in invalid_records:
   
    display_name = record['name'] if record['name'] else "Unknown User"
    print(f"{display_name} --> Reason: {', '.join(record['reasons'])}")