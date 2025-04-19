# string_calculator_TDD# 🧮 String Calculator TDD Kata (Python)

A simple calculator that adds numbers provided in a specially formatted string.  
This project is built using **Test-Driven Development (TDD)** and `unittest`.

---

## ✅ Features

- Returns `0` for an empty string
- Returns the number itself for a single number
- Adds multiple numbers separated by commas or newlines
- Supports a **custom single-character delimiter**, e.g. `//;\n1;2`
- Throws a `ValueError` if any **negative numbers** are included, listing them in the message


## ✅ Extra Features

- **Ignores numbers > 1000**, e.g. `2 + 1001 = 2`
- Supports **delimiters of any length**, e.g. `//[***]\n1***2***3`
- Supports **multiple delimiters**, e.g. `//[*][%]\n1*2%3`
- Supports **multiple delimiters of any length**, e.g. `//[***][%%]\n1***2%%3`
---

## 🧪 Sample Test Cases

```python
add("")                       # ➞ 0
add("1")                      # ➞ 1
add("1,2")                    # ➞ 3
add("1\n2,3")                 # ➞ 6
add("//;\n1;2")              # ➞ 3
add("1,-2,-5")                # ➞ ValueError: negative numbers not allowed -2, -5
add("2,1001")                 # ➞ 2
add("//[***]\n1***2***3")    # ➞ 6
add("//[*][%]\n1*2%3")       # ➞ 6
add("//[***][%%]\n1***2%%3") # ➞ 6
```

## 🚀 How to Run
### 🔧 Prerequisites
- Python 3.7+
- (Optional) Virtual environment

## 📦 Install dependencies
- No external dependencies required — uses built-in `unittest`.

## 🧪 Run all tests
Using unittest:
```bash
python -m unittest discover -s tests
```