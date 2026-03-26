numbers = [10, 15, 20, 25, 30]

def divisible_by_10(numbers_list):
    """
    Returns a list of numbers from numbers_list that are divisible by 10.
    """
    return list(filter(lambda x: x % 10 == 0, numbers_list))

result = divisible_by_10(numbers)

print(result)