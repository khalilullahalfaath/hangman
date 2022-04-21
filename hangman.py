import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words) #select random word from words list
    while "-" in word or " " in word:
        word = random.choice(words) #select random word from words list
    return word.upper()

def hangman():
    word = getValidWord(words)
    print(word)
    wordLetters = set(word) #make the letter in words into set
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() #word that the user has guessed

    lives = 6

    #getting user input
    while len(wordLetters) > 0 and lives > 0:
        # letters used and lives
        print("You have",lives)
        print("You have used these letters: ", ' '.join(usedLetters))

        #what current word is
        wordList = [letter if letter in usedLetters else "-" for letter in word]
        print("Current word: ", ' '.join(wordList))

        userLetter = input("Guess a letter: ").upper() #make every letter that user input to uppercase
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives = lives-1
                print("Letter is not in word")
        elif userLetter in usedLetters:
            print("You have already used that character. Please try again")
        else:
            print("Wrong letter. Try again")
    
    if lives == 0:
        print("You died. The word was",word)
    else:
        print("You guessed the word",word,"!!")

hangman()