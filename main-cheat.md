# Crypticode Cheatsheet for main.py
You can't look at the internet during Crypticode, but you can ask your partner and use this cheat-sheet.

## Mission

### Goals
You're in charge of interacting with the user via the command line.  
Quickly fill in the code for [main.py](main.py)!
You must accept input from the user (guessed letters) and display output (known letters, guessed letters, etc.) to make a game of hangman function properly!

### Working Together
First and foremost, **DON'T** share code with each other.  
Don't look at your partner's code or at their starter file, as this ruins the challenge!

With that being said...  
You're working on [main.py](main.py) and your partner is writing back.py.  
Your file is run and connects with back.py in order to access its function definitions.  
Without your work, the program will break!

Note that not all of the concepts on this cheat sheet are needed for your program. It's mainly meant as a refresher of Python for those needing it.

## Important

### User Interface
`print(data)`  
`string = input(string)`  
The print() function sends data to standard output and returns nothing.  
The input() function sends a prompt to standard output and returns the user's standard input.
```
print("Possible options:\n" + my_list)
user_choice = input("Your selection: ")
```

### Accessing back.py
`import data`
`data.function()`  
Your partner is writing function definitions in the back.py file.  
Import back.py to access your partner's work.  
Specify when a function comes from there.  
```
import back.py
# This allows you to access you partner's work

titles, contents = data.read_file()
```

### Functions from back.py
Ask your partner about what functions they have available on back.py.
Pay attention to the arguments needed for each function. 

### While Loop
`while condition:`  
This loop continues until a condition is met.  
Use it to prevent the program from continuing until the user gives an acceptable answer.  
```
user_input = ""
while user_input != "y" and user_input != "n":
    user_input("Yes or no? (y/n)")
if user_input == "y":
    print("Yes received.")
elif user_input == "n":
    print("No received.")
``` 

### If Statement
`if condition:`  
`elif condition:`  
`else:`  
Checks whether a condition is true to decide which code to run.  
It's the crux of programming and is useful in every scenario imaginable.  
```
user_choice = input("What would you like to do next? ")
if user_choice == "read":
    data.read_file()
elif user_choice == "write":
    # Ask user what to write
    data.write_file(title, contents)
else:
    print("I didn't understand that.")
```

### Exit Program
`exit()`  
Immediately terminates the program.  
Useful for closing the program cleanly when user is done using it.
```
user_choice = input("All done? (y/n)\n")
if user_choice.lower() == "y":
	print("Goodbye!")
	exit()
```

## Functions

### Definition
`def func_name(args):`  
You'll define several of your own functions.  
Useful for keeping your code clean.  
```
def example_add(arg1, arg2):
	print("I'll go ahead and add those together")
	value = int(arg1) + int(arg2)
	print(value)
	return value
```

### Lowercase
`string = string.lower()`  
Returns input string in lowercase.  
Useful for accepting case-insensitive user input.  
```
user_choice = input("Would you like to continue? (y/n)\n")
if input.lower() == "y":  
	pass  
else:
	exit()
```

### Datatype Casting
`integer = int(data)`  
`string = str(data)`  
`list = lst(data)`  
Functions that return the inputted argument in the requested datatype.  
Useful for converting user input to a number, for instance.
```
user_choice = int(input("Select a number from the given options.\n"))
print(options[user_choice])
```

## Statements

### Pass
`pass`  
Skips an empty code block without an error.  
Useful for leaving behind loops, functions, etc to fill in later.
```
while True:
	# I'll fill this loop in later
	pass
```

### Break
`break`  
Immediately exits a loop, even if its condition is not met.  
It's especially useful when inside an if statement.
```
while True:
	user_choice = input("Wanna exit this vicious cycle? (y/n)\n")
	if user_choice == "y":
		print("Let's get out of here!")
		break
		print("This code will not run.")
print("We're finally out!")
```

### Continue
`continue`   
Skips to the next iteration of a loop.  
In a for loop, the counter variable will increment as usual.  
```
# This code will just print "5"
for i in range(6):
	if i < 5:
		continue
	print(i)
```

## Operators

### Logical Operators
`and`  
`or`  
`not`  
And returns True if both statements are True.
Or returns True if any statement is True.  
Not returns the opposite of what it's given.   
```
if this == 1 or that == 1:
	if not(this == 2 or that == 2):
		print("Passed both if statements")
```

### Equality Operators
`==`  
`!=`  
These can check whether two values are equal (==) or not equal (!=) to each other.  
Useful for checking conditions in if statements & loops.
```
something = "this"
if something == "this":
    print("It's this")
if something != "that"
    print("It's not that")
```

### Inequality Operators
`<`  
`>`  
`<=`  
`>=`  
Just like in math, they check whether one value is greater (>) or less than (<) another.  
The equals signs give True even when the values are equal to each other.
```
user_choice = int(input("Pick a number: "))
if user_choice > 5:
    print("It's greater than five")
if user_choice < 3:
    print("It's lesser than three.")
```

### Basic Math
`/`  
`*`  
`+`  
`-`  
These operators work just like math symbols.
```
print(3 + 2) -> 5
print(3 - 2) -> 1
print(3 * 2) -> 6
print(3 / 2) -> 1.5
```

### Modulo
`%`  
Gives the remainder of a division operation.  
Useful for determining whether a number is even.  
```
if (number % 2 == 0):
    print(str(number) + "is even!")
else:
    print(str(number) + "is odd!")
```

### Exponent
`**`  
Raises a number to a power.  
```
print(10 * 3) -> 1000
```
