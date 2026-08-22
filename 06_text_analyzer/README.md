# 📝 Text Analyzer

A beginner Python program that analyzes a piece of text and provides basic statistics about it.

## 📌 Features

- Counts characters
- Counts words
- Counts vowels
- Counts consonants
- Displays the results in a structured format

## 🧠 Concepts Used

- Strings
- String methods
- `split()`
- `len()`
- `lower()`
- `isalpha()`
- `for` loops
- `if / else`
- Dictionaries
- `.items()`
- Counting with variables

## ▶️ How to Run

Run the program using:

bash
python text_analyzer.py

Enter a sentence or paragraph when prompted.

💻 Example
Enter your text: Python is fun!

Text Analysis 
Characters: 15
Words: 3
Vowels: 3
Consonants: 8
🔍 How It Works

The program first accepts text from the user.

The split() method separates the text into words:

words = text.split()

The program then loops through each character and checks whether it is a vowel or consonant.

for char in text.lower():

The results are stored in a dictionary:

analysis = {
    "Characters": character_count,
    "Words": word_count,
    "Vowels": vowels,
    "Consonants": consonants
}

Finally, the dictionary is displayed using:

for key, value in analysis.items():
🎯 Purpose

This project was created to practice working with strings, loops, dictionaries, and basic text processing in Python.
