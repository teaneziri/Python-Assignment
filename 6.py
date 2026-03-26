def find_longest_line(file_path):
    """
    Reads a file and returns the longest line along with its length.
    Handles file not found and empty file errors.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            if not lines: 
                print("The file is empty.")
                return None
            
            
            longest_line = max(lines, key=lambda line: len(line.strip()))
            print(f"Longest line ({len(longest_line.strip())} characters):\n{longest_line.strip()}")
            return longest_line.strip()
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None



file_path = r"C:\Users\teane\Downloads\konfigurime (1).txt" 
find_longest_line(file_path)