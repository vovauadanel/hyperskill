# Write your code here
import random

print("H A N G M A N")
word = input("Guess the word: ")
right_words = ["python", "java", "kotlin", "javascript"]
if word == random.choice(right_words):
    print("You survived!")
else:
    print("You lost!")
