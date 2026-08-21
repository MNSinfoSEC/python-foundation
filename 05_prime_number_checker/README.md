# 🔢 Prime Number Checker

A beginner Python program that checks whether a given number is a prime number.

## 📌 Features

- Accepts a number from the user
- Checks whether the number is prime
- Handles numbers less than 2
- Uses a loop to test possible divisors
- Returns a clear result

## 🧠 Concepts Used

- Functions
- User input
- int() type conversion
- if / else
- for loops
- range()
- % modulo operator
- Boolean values
- return

## ▶️ How to Run
Run:

bash
python prime.py


Enter a number when prompted.
💻 Example
Enter a number: 17
Prime number! ✅

Another example:

Enter a number: 20
Not a prime number. ❌
🔍 How It Works

The program checks whether the number can be divided evenly by any number between 2 and the number before it.

The modulo operator:

number % i

returns the remainder.

If the remainder is 0, the number has another divisor and therefore is not prime.

🎯 Purpose

This project is part of my python-foundation repository and was created to strengthen my understanding of loops, functions, conditions, and logical problem-solving in Python.
