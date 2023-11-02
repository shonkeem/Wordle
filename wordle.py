from tkinter import NONE
import nltk
import random
from colorama import Fore, Back, Style
from termcolor import colored, cprint
from nltk.corpus import words
nltk.download('words')

master_word_list = words.words()

# Wordle Game
'''
1. Get a random 5 Letter word from the word list
2. User guesses a 5 letter word
3. Checks which letters are in the word
4. Checks which letters are in the word and in the correct position
5. If the user guesses the word correctly, they win
6. If the user guesses the word incorrectly, iterate again starting from step 2 until they guess the word correctly or 6 steps
'''

def check_in_word(word, letter):
    if letter in word:
        return True
    else:
        return False


# pick random 5 letter word
word_list = []
for i in master_word_list:
    if len(i) == 5:
        word_list.append(i.lower())
# user guesses a 5 letter word
print(len(word_list))

def guess_word():
    guess = input("Guess a 5 letter word: ").lower()
    if len(guess) != 5:
        print("\nPlease enter a 5 letter word!\n")
        return None
    elif guess not in word_list:
        print("\nNot In Word List!\n")
        return None
    else:
        return guess


def check_guess(word, guess):
    output = {}
    for i in range(len(word)):
        if word[i] == guess[i]:
            output[i] = 'green'
        elif guess[i] in word:
            output[i] = 'yellow'
        else:
            output[i] = 'gray'
    return output


def output_results(results, guess):
    output = ""
    for i in range(len(word)):
        if results[i] == 'green':
            output += f"\u001b[32m {guess[i]}"
        elif results[i] == 'yellow':
            output += f"\u001b[33m {guess[i]}"
        else:
            output += f"\u001b[37m {guess[i]}"
    output += "\u001b[0m"
    return output


print("Welcome to Wordle!")
word = random.choice(word_list)
print(word)

i = len(word)+1
while i != 0:
    guess = guess_word()
    if guess != None:
        results = check_guess(word, guess)
        k = output_results(results, guess)
        print(k)
        values = results.values()
        if len(set(values)) == 1 and 'green' in values:
            print("You Win!")
            print(f"Attempt #: {len(word)+2-i}")
            break
        i -= 1
    if i == 0:
        print("You Lose!")
