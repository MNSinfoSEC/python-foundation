# 🔄 Palindrome Checker

A beginner Python program that checks whether a word reads the same forwards and backwards.

## 📌 Features
- Accepts a word from the user
- Converts input to lowercase
- Reverses the string
- Compares the original and reversed strings
- Identifies whether the input is a palindrome

## 🧠 Concepts Used

- Functions
- User input
- Strings
- `.lower()`
- String slicing
- `[::-1]`
- `return`
- `if / else`

## ▶️ How to Run

Run:

bash
python palindrome.py

Enter a word when prompted.

💻 Example
Enter a word: madam
Palindrome! ✅

Another example:

Enter a word: python
Not a palindrome. ❌
🔍 How It Works

The program reverses the input using:

text[::-1]

It then compares the original text with the reversed text.

If both are identical, the word is a palindrome.

🎯 Purpose

This project is part of my python-foundation repository and was created to strengthen my understanding of functions and string manipulation in Python.
