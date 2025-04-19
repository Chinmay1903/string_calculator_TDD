def add(numbers: str) -> int:
    if numbers == "":
        return 0
    number_list = numbers.split(",")
    return sum(int(n) for n in number_list)
