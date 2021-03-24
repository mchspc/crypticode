# Crypticode Cheatsheet for main.py
You can't look at the internet during Crypticode, but you can ask your partner and use this cheat-sheet.

## Mission

### Goals
You're in charge of reading & writing a text file with data.  
Quickly fill in the function definitions from [data.py](data.py)!
- Open data file at startup
- Close data file when done
- Read data from file
- Turn that data into list(s)  
- Write new data to file

### Working Together
First and foremost, **NEVER** share code with each other.  
Don't look at your partner's code or at their starter file, as this ruins the challenge!

With that being said...  
You're working on [data.py](data.py) and your partner is writing main.py.  
Your file is not run, but it contains function definitions accessible to main.py at runtime.  
Without your work, the program will break!

## Important

### File Management
`import os` 
`file_var = open(filepath, permission)`  
`string = file_var.read()`  
`file_var.write(string)`  
`file_var.close()`  
You must import the os module to use these functions, which let you save and read text documents.  
The open() function saves your file as a variable.  
The read() and write() function let you access and save data respectively.  
The close() function should be used before the program closes.
```
print("Possible options:\n" + my_list)
user_choice = input("Your selection: ")
```

### For Loop
`for i in iterable:`  
This loop executes the given code once per item in an iterable such as a range, list, or string.  
Use it to complete similar actions in rapid succession.
```
current = ""
for char in text:
	if char == "\n":
		my_list.append(current)
		curent = ""
	else:
		current += char
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
    data.read_file(recfile)
elif user_choice == "write":
    # Ask user what to write
    data.write_file(title, contents)
else:
    print("I didn't understand that.")
```

### Split
`list = string.split(divider)` 
Turns a string into an array using a divider character.  
Useful for converting file contents into a list.  
```
recfile_contents = recfile.read()  
lines = recfile_contents.split("\n")
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

### Range
`list = range(start, stop, step)`  
Returns a list of numbers beginning at start, incrementing by step, and ending at (but not including) stop.  
The start and stop arguments are optional, defaulting to 0 and 1 respectively.  
```
user_choice = int(input("Select option 0, 1, or 2 please: "))
if user_choice in range(3):
	break
else:
	print("You did not select a valid option.\n")
```

### Item Length
`int = len(iterable)`  
Returns the number of items in an iterable such as a range, list, or string.
Useful when specifying the number of available options.
```
num_notes = len(notes)
print("You have" + num_notes + "notes available.\n")
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