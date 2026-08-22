# Text Analyzer
# Python Foundation - Project 06

text = input("Enter your text: ")

words = text.split()

word_count = len(words)
character_count = len(text)

vowels = 0
consonants = 0

for char in text.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

analysis = {
    "Characters": character_count,
    "Words": word_count,
    "Vowels": vowels,
    "Consonants": consonants
}

print("\n--- Text Analysis ---")

for key, value in analysis.items():
    print(key + ":", value)
