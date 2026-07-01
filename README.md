In this project, I built a reliable command-line calculator using Python. I implemented robust input validation using try-except blocks to 
catch ValueError and handled logic flows with conditional if-elif statements.
I also used structured while loops to manage user retries for invalid operators and to dynamically prevent ZeroDivisionError during division.
# Simple CLI Calculator with Error Handling

A robust command-line calculator built with Python that performs basic arithmetic operations while handling user input errors and preventing system crashes.

## Features
* **Basic Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Input Validation:** Prevents crashes from invalid inputs (e.g., entering letters instead of numbers).
* **Safe Division:** Automatically catches and handles division-by-zero errors by prompting the user for a valid number.
* **Strict Operator Control:** Ensures the user can only proceed by entering valid arithmetic operators.

## Technical Concepts Used (What's Under the Hood)
In this project, I implemented several core Python concepts to ensure smooth execution:
* **Exception Handling (`try-except`):** Used to catch `ValueError` during user input, preventing the program from crashing when non-numeric values are entered.
* **Input Validation Loops (`while` loops):** Keeps prompting the user until valid inputs (both for numbers and operators) are provided.
* **Conditional Logic (`if-elif` statements):** Directs the program to perform the correct mathematical operation based on user choice.
* **Dynamic Variable Re-assignment:** Safely updates the denominator value if the user initially enters zero during division.

## Preview
```text
Enter number: 10
Choose an operator ('+', '-', '/', '*'): /
Enter number: 0
Cannot divide by zero! Please enter a different number.
Enter number: 2
10.0 / 2.0 = 5.0
```
