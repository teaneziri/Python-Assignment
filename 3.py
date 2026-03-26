class InvalidAgeError(Exception):
    """
    Raised when age < 0 or age > 120.
    """
    pass


def validate_age(age):
    """
    Takes an age as input.
    Raises InvalidAgeError if age < 0 or age > 120.
    Returns "Valid age" if age is within the valid range.
    """
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120")
    else:
        return "Valid age"



try:
    user_input = int(input("Enter your age: "))  
    result = validate_age(user_input)
    print(result)
except InvalidAgeError as e:
    print(f"Invalid age: {e}")
except ValueError:
    print("Invalid input: Please enter a valid age.")
