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
    int_numbers = []
    negative_numbers = []

    for num in number_list:
        if num.strip():
            n = int(num)
            if n < 0:
                negative_numbers.append(n)
            elif n <= 1000: 
                int_numbers.append(n)

    if negative_numbers:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negative_numbers))}")

    return sum(int_numbers)
