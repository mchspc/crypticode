import data

# To access your partner's functions, use data.<functionname>()
# Ask your partner what their functions are called and what they do

'''
Goals of this file:     
Interact with user
Ask if they'd like to read or to write
If read, display all titles and allow to select one (Access functions from data.py)
When selected, display title and full text to user

If write, receive user input for title and text and use data.py functions to write to .txt

Good luck!
'''

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