wordList = [
    "apple",
    "banana",
    "cherry",
    "dog",
    "elephant",
    "flamingo",
    "giraffe",
    "happiness",
    "icecream",
    "jazz",
    "kangaroo",
    "lemon",
    "monkey",
    "noodle",
    "octopus",
    "penguin",
    "quokka",
    "rainbow",
    "strawberry",
    "tiger",
    "umbrella",
    "violet",
    "watermelon",
    "xylophone",
    "zebra",
    "blue",
    "red",
    "green",
    "yellow",
    "orange",
    "purple",
    "brown",
    "pink",
    "black",
    "white",
    "ocean",
    "forest",
    "desert",
    "mountain",
    "valley",
    "river",
    "island",
    "moon",
    "sun",
    "star",
    "planet",
    "galaxy",
]

import string
import random

def print_welcome_messages():
    print("-----Welcome, Pizza Lover!-----")
    print("Guess the letters of the hidden word! Use pizza slices as fuel, therefore your guesses are limited...")

def pick_difficulty():
    pickedDifficulty = ""
    
    while True:
        pickedDifficulty = input("Please select the difficulty: Beginner / Easy / Medium / Hard: ").lower()
        if pickedDifficulty in ["beginner", "easy", "medium", "hard"]:
            break
        
    return pickedDifficulty
    
def is_guess_valid(input):
    return len(input) == 1 and input in string.ascii_letters

def populate_revealedWordList_based_on_guess(guess, secretWord, revealedWordList):
    for i in range(0, len(secretWord)):
        if secretWord[i] == guess:
            revealedWordList[i] = guess
    return revealedWordList

def try_restart_game():
    if input("Do you want to restart ? (y/n): ") == "y":
        start_game()
    else :
        exit()
 
def start_game():
    difficulty = pick_difficulty()
    
    secretWord = random.choice(wordList)
    
    remainingPizzaSlices = 0
    match difficulty:
        case "easy":
            remainingPizzaSlices = len(secretWord) + 2
        case "medium":
            remainingPizzaSlices = len(secretWord)
        case "hard":
            remainingPizzaSlices = len(secretWord) - 2
        case "beginner":
            remainingPizzaSlices = -1 # No limit

    hiddenLetterCharacter = "*"
    revealedWordList = [hiddenLetterCharacter] * len(secretWord)
    print(f"Your word is: {''.join(revealedWordList)}")
    
    wrongGuesses = []
        
    while hiddenLetterCharacter in revealedWordList:
        guess = ""
        while not is_guess_valid(guess):
            guess = input("Please make a guess: ") 
        
        if not (guess in secretWord) and (guess not in wrongGuesses):
            wrongGuesses.append(guess)
            remainingPizzaSlices -= 1
            
        revealedWordList = populate_revealedWordList_based_on_guess(guess, secretWord, revealedWordList)
            
        revealedWord = "".join(revealedWordList)
        print(revealedWord)
        
        print(f"You have already tried: {', '.join(wrongGuesses)}")
        
        if remainingPizzaSlices > 1:
            print(f"Remaining pizza slices: {remainingPizzaSlices}")
        elif remainingPizzaSlices == 0: 
            print("You have lost all your pizza slices :(")
            print(f"The word was {secretWord}")
            
            try_restart_game()
            
    print(f"Congrats! You guessed the word '{secretWord}'")
    if remainingPizzaSlices > 1:
            print(f"Remaining pizza slices: {remainingPizzaSlices} :)")
    try_restart_game()
   
# Main:
print_welcome_messages()

start_game()