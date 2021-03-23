'''
You are in charge of interacting with the user via the command line
You can access your partner's functions by writing data.function()

Refer to this cheat-sheet for help!
https://github.com/mchspc/crypticode/blob/main/main-cheat.md

Goals
-----
- Interact with user
- Ask if they'd like to read or to write
- If read, display all titles and allow to select one (Access functions from data.py)
- When selected, display title and full text to user

Good luck!
'''
import data

while (True):
    recfile = data.startup() #assigns recfile variable to the output of startup() command, use recfile as the first argument in the other data.py functions
    userinput = input("")


    '''
    Write all if statements here
    '''
    else:
        '''
        Call shutdown and exit the program
        '''
    # Write a set of if statements to read, write, or close the program based on userChoice (be prepared to handle edge cases)
    # Tip: Call the shutdown() function from data.py before exit() when ending the program read_file()