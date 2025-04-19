import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    delimiter = ",|\n"  # default delimiters

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:]) 
        numbers = parts[1]
    
    number_list = re.split(delimiter, numbers)
    return sum(int(n) for n in number_list)
