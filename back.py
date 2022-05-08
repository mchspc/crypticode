from csv import reader
from random import choice

# Variable assignments
words = []
random_word = ""
known_letters = []
guessed_letters = []
guesses = 0

def ReadBank():
    # Populate list with contents of word bank file (no change needed)
    global words

    with open("word-bank.csv", newline='') as word_bank:
        read_words = reader(word_bank, delimiter=',')
        for word in read_words:
            words += word

def RandomWordSelection():
    # Use a function from the random module to select a random word
    # Populate the known_letters list with a _ for each letter

def AlreadyGuessed(guessed_letter):
    # Return letter if already guessed, nothing if not (no change needed)
    return guessed_letter in guessed_letters

def LetterInWord(guessed_letter):
    # Check if the given letter is in the word
    # If it is, replace the _ in known_letters with the letter
    # If not, increase the guesses counter by 1

def GetWord():
    # Return the random word selected from bank (no change needed)
    return random_word

def GetKnownLetters():
    # Return the contents of known_letters as a string (no change needed)
    return "".join(known_letters)

def GetGuessedLetters():
    # Return the contents of guessed_letters as a string (no change needed)
    return " ".join(guessed_letters)

def GetTimesGuessed():
    # Returns times guessed (no change needed)
    return guesses

def HasWon():
    # Checks if met winning condition (no change needed)
    return "".join(known_letters) == random_word
