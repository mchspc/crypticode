import back

def DrawStickman(state):
    if state == 0:
        print("\n\t|―――――\n\t|  |\n\t|\n\t|\n\t|\n\t|\n\t――――――――――――――――")
    elif state == 1:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t|\n\t|\n\t|\n\t――――――――――――――――")
    elif state == 2:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t|  |\n\t|\n\t|\n\t――――――――――――――――")
    elif state == 3:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t| -|\n\t|\n\t|\n\t――――――――――――――――")
    elif state == 4:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t| -|-\n\t|\n\t|\n\t――――――――――――――――")
    elif state == 5:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t| -|-\n\t| /\n\t|\n\t――――――――――――――――")
    elif state == 6:
        print("\n\t|―――――\n\t|  |\n\t|  O\n\t| -|-\n\t| / \ \n\t|\n\t――――――――――――――――")

def GuessingPhase():
    # Checks whether to continue game & sends player input to guessed letters list
    while back.GetTimesGuessed() < 6:
    # For <6 guesses, continue by displaying guessed letters & asking for new letter

    # If 6 guesses reached, end the game by calling appropriate function

def StartGame():
    # Call back.py functions for reading word bank & picking a random word 
    # Begin the guessing phase by calling the apppriate function

def GameEnd(won):
    # Reveal the correct word with the help of a back.py function
    # Tell whether the player won & end the script

# Call StartGame() at the beginning (no change needed)
StartGame()
