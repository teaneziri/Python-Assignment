values = ["5", "10", "x", "15", "NaN", "20"]

def clean_numeric_data(values_list):
    """
    Converts valid numbers in the list to integers.
    Skips invalid values.
    Returns a list of cleaned integers.
    """
    cleaned = []
    for v in values_list:
        try:
            cleaned.append(int(v))
        except ValueError:
            continue
    return cleaned


cleaned_values = clean_numeric_data(values)

print(cleaned_values)