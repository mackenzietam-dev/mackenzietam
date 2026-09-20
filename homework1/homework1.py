# File: homework1   

# --- Variables and Data Types ---

a = 10 
print (a)
print (type(a)) # a is an integer

b = 1.5
print (b)
print (type(b)) # b is a float

c = 3j
print (c)
print (type(c)) # c is a complex number

d = "hello"
print (d)
print (type(d)) # d is a string

e = [1, 2, 3]
print (e)
print (type(e)) # e is a list 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print (type(f)) # f is a dictionary

g = (1, 2)
print (g)
print(type(g)) # g is a tuple

h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) # h is a list

i = True
print (i)
print(type(i)) # i is a boolean

j = None
print (j)
print(type(j)) # j is a NoneType

k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list

l = str(14)
print (l)
print (type(l)) #l is a string

m = 1e4
print (m)
print (type(m)) #m is a float

'''
1. How many different data types did you find?

I found 9 different types.

2. List all the data types you found.

integer
float
complex
string 
list
dictionary 
tuple
boolean
NoneType

3. What variables have the same data types?

b and m are floats
d and l are strings
e, h, and k are lists

4. What was the data type of l? Why is it not an integer? What does str() do?

l was intially an integer without the str() function; it got converted into a string.

5. Look up one more data type not given above. Repeat the same procedure.

'''

n = {1, 2, 3}
print(n)
print(type(n)) # n is a set

# 3.2

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False 10 is not eq to 9
print(10 <= 9) # False 10 is not eq or less than 9 
print(bool("abc")) # True, there are characters within str function
print(bool(123)) # True because it is a nonzero number 
print(bool(["apple", "cherry", "banana"])) # True bc list is not empty
print(bool(True)) # True because value is True
print(bool(False)) # False becasue value is False 
print(bool(0)) # False because its a zero
print(bool("")) # False bc string is empty
print(bool(" ")) # True because string has a space within it 
print(bool(())) # False because tuple is empty
print(bool([])) # False because list is empty
print(bool({})) # False because dict is empty
print(bool(True and False)) # False because the "and" must be True 
print(bool(True and True)) # True, double True
print(bool(False and False)) # False, double false
print(bool(True or False)) # True because or only requires one value of True to be overall True
print(bool(True or True)) # True because at least one value is True
print(bool(False or False)) #False because neither value is True
print(bool(not(False))) # True, double negative
print(bool(not(True))) # False, negative into positive 

''' 

Questions:
• What pattern do you notice about expressions returning True or False?

I noticed that non empty values and non zero numbers are True, while the opposite of that is False

• Which expression surprised you about its result?

None

• Create an expression, not given above, that will return True. Why is it True?

print(bool(1)) - because there is a nonzero value

• Create an expression, not given above, that will return False. Why is it False?

print(bool(0.0)) - because there is a zero value

'''

# 3.3.1

print(10 + 5) # 15, + performs addition
print(10 - 5) # 5 performs subtraction
print(2 * 4) # 8 performs multiplication
print(6 / 3) # 2 performs division 
print(5 % 2) # 1 gives remainder after division
print(3 ** 2) # 9 does 3^2
print(15 // 2) #7, gives result after division, dropping result decimal point

# 3.3.2

print(5 == 2) # False 5 is not eq to 2
print(10 != 10) # False 10 is eq to 10
print(2 < 5) # True 5 is greater than 2
print(12 > 5) # True 12 is greater than 5
print(5 <= 6) # True 5 is less than or equal to to 6
print(1 >= 10) # False 1 is not greater than or equal to 10

# 3.3.3

x = 5

x +=5
print (x)

x-=4
print (x)

x*=3
print (x)

''' 

1. What does the operator and do? Write an expression that results in True. Write an expression
that results in False.

And returns True only if both conditions are both true. 

print (True and True) would be True
print (True and False) would be False

2. What does the operator or do? Write an expression that results in True. Write an expression
that results in False.

The or operator returns True if at least one condition is true

print (True or False) would be True
print (False or False) would be False

3. What does the operator not do? Write an expression that results in True. Write an expression
that results in False. 

The not operator reverses the value
print (not False) would be True
print (not True) would be False

More Questions

1. What is the difference between / and //?

/ does standard division whilst // divides and removes the any tailing decimal 

2. What is the difference between % and //?

% gives the remainder after division and // divides and removes the any tailing decimal 

3. What operator would you use to calculate the remainder when dividing two numbers? Give
an example.

I would use %, for example 7%2 would be 1

4. How do assignment operators work?

assingment operators change the value of a variable 

'''

# 3.4 

my_string = "hello"

print(my_string) # prints hello
print(my_string[0]) # prints h 
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o (last character)
print(my_string[1:3]) # prints el
print(my_string[0:5:2]) # prints hlo
print(len(my_string)) # prints 5
print(my_string + "goodbye") # prints hellogoodbye
print(my_string * 7) # prints hellohellohellohellohellohellohello

# 3.4.1

''' 
1. Define the term slicing. For which of the manipulations did you slice your string?

I used slicing in my_string[1:3] and my_string[0:5:2].

2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)

Hello, my name is Oski

3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")

Hello, my name is Oski

4. What is the difference between the two last print statements?

The second one using an f string which puts the variable inside the actual string which the first doesnt

'''

# 3.5

''' 

# cd
# changes directory
# example: cd Desktop

# ls
# list files and folders in current directory
# Example: ls

# ls -a
# lists all files and folders including hidden ones
# Example: ls -a

# mkdir
# creates new directory.
# Example: mkdir homework1

# cat
# displays contents of file
# Example: cat homework1.py

# pwd
# shows full path of the current directory.
# Example: pwd

# cd ..
# moves up one directory
# Example: cd ..

# cd .
# refers to current directory
# Example: cd .

# cd ~
# moves to home directory
# Example: cd ~

# cp
# copies a file or folder
# Example: cp homework1.py homework1_copy.py

# mv
# moves or renames a file.
# Example: mv old.txt new.txt

# rm
# deletes file.
# Example: rm old.txt

# clear
# clears the terminal screen
# Example: clear

# grep
# Searches for text inside a file.
# Example: grep "hello" homework1.py

Questions:
1. Look up 3 other commands not present. Define and explain how to use them on the command
line.

# touch
# creates a new empty file
# Example: touch notes.txt

# nano
# opens a file in Nano text editor so you can view or edit it in the terminal
# Example: nano homework1.py

# head
# shows the first few lines of a file
# Example: head homework1.py

2. What is the difference between ls and ls -a?

ls -a shows everything that ls does but also the hidden files and folders

3. What is a hidden file?

A file that starts with a period and does not normally appear when using ls
# Example: .gitignore

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.

-l
used with ls to show more detailed info about files
Example: ls -l

-h
makes file sizes easier to read when used with certain commands
Example: ls -lh

-r
reverses order of results when used with certain commands
Example: ls -r

'''