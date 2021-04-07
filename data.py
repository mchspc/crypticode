'''
You are in charge of reading & writing data from a text file
Functions you define here will be accessible from your partner's script

Refer to this cheat-sheet for help!
https://github.com/mchspc/crypticode/blob/main/data-cheat.md

Goals
-----
- Read data from single file
- Separate that data (titles & notes) into lists (separated by new line operator)
- Return titles and content as separate lists
- Write new data to the file
- Close data file at the end of all functions

Good luck!
'''

def startup():
    recfile = open("recfile.txt", "a")
    recfile.close()
    # Ignore - Required for testing purposes
def read_file():
    # open file with appropriate permissions
    # read from file
    # separate the titles & content so it can be returned to main.py
    # close file after
    return(titles, content)

def write_file(new_title, new_content):
    # open file with appropriate permissions
    # write new data (from args)
    # organize it so it can be re-read (consistent with methods in read_file())
    # close file after