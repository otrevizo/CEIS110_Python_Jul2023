#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:31:19 2021

@author: otrevizo

Vignettes for CEIS110 based on zyBooks Python code

This file contains code copied directly from zyBooks.

It also contains script modifications based on python.prg
Consult https://docs.python.org/3/

The objective is to guide students from CEIS110 to learn Python.
This script is purely for persoal and educational uses.
This code is not intended to be published or used outside of the classroom.

"""

# %% Libraries and packages

import math
import datetime
import random

import matplotlib.pyplot as plt

import numpy as np

# Creating named tuples
from collections import namedtuple

# import filename as something -- do not enter filename.py, just filename
import my_vignette_library as my

# %% help()

# Always use help(`function` or `library`)

help(type)


# %% M1: Variable types: strings, integers, and float

s = "abcd"

i = 5

f = 3.1416

type(s)

type(i)

type(f)

id(s)

id(i)

id(f)

# %%% Strings
# From zyBooks Ch. 1 and 2

# Basic strings
my_string1 = '123'
print(my_string1)

my_string2 = 'abc'
print(my_string2)

my_string3 = 'abc123'
print(my_string3)

my_string4 = 'abc 123 ABC 456'
print(my_string4)

# Accessing individual characters in a string
# Each character is indexed
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Note: index begins with 0 (zero)
print(alphabet[0], alphabet[1], alphabet[25])

# String concatenation
concatenated_string = my_string1 + my_string2
print('Easy as ' + concatenated_string)

# %%% String format()
# String formatting based on zyBook Ch 2.11, using {} brackets
'''
https://docs.python.org/3/library/string.html#formatspec

Type 	Description     Example
s  String (default)   '{:s}'.format('Aiden') output = Aiden
d  Decimal (integers) '{:d}'.format(4) output = 4
b  Binary (integers)  '{:b}'.format(4) output = 100 (4 in binary)
x, X Hexadecimal in lowercase (x) and uppercase (X) (integer alues only)
   '{:x}'.format(15) output = f
e Exponent notation   '{:e}'.format(44) output = 4.400000e+01
f  Fixed-point (6 pl) '{:f}'.format(4) output = 4.000000
.[precision]f 	Fixed-point notation (programmer-defined precision)
                      '{:.2f}'.format(4) outout = 4.00
'''

help(format)

# Names some strings
first_name = 'John'
last_name = 'Doe'

# You can also predefine the string as follows, ready for format
my_string5 = "First name is {0}, last name is {1}"

# And notice how the dot "." works to build up the operations
my_string5.format(first_name, last_name)


number = 6
amount = 32
print('{} burritos cost ${}'.format(number, amount))

# Positional replacement
print('The {1} in the {0} is {2}.'.format('hat', 'cat', 'fat'))

# Inferred replacment
print('The {} in the {} is {}.'.format('hat', 'cat', 'fat'))

# Named replacement example 1
print('The {animal} in the {headwear} is {shape}.'
      .format(headwear='hat', animal='cat', shape='fat'))

# Named replacement example 2
print('The {animal} in the {headwear} counts to {x}.'
      .format(headwear='hat', animal='cat', x=5))


print("{}'s last name is {}".format(first_name, last_name))

# Note: values start counting with 0 (zero)
print("First name is {0}, last name is {1} ".format(first_name, last_name))

# Or just send the operations to the console
'{:s} ${:.2f} tacos is ${:.2f} total'.format('Three', 1.50, 4.50)

'{0:s} ${2:.2f} tacos is ${1:.2f} total'.format('Three', 4.50, 1.50)

# And run operations even within the arguments as Python does on functions
'{cnt:s} ${cost:.2f} tacos is ${sum:.2f} total'.format(cnt='Three',
                                                       cost=1.50,
                                                       sum=3 * 1.50)

# Build the string first, then use it
my_string6 = "{cnt:s} ${cost:.2f} tacos is ${sum:.2f} total"
my_string6.format(cnt='Three', cost=1.50, sum=3 * 1.50)


# %%% Integers

my_int = int('123')
print(my_int)

# %%% Convert str to int

print('Enter wage:', end=' ')
wage = int(input())

new_wage = wage + 10
print('(adding 10) New wage:', new_wage)

# %%% Convert str to float
"""
Function 	Notes 	Can convert:
int() 	Creates integers 	int, float, strings w/ integers only
float() 	Creates floats 	int, float, strings w/ integers or fractions
str() 	Creates strings 	Any
"""

input_text = input('Enter a number:\n')
float_variable = float(input_text)

# %%% Convert float to int

int_variable = int(float_variable)

print('original input text:', input_text)
print('input text converted to a float:', float_variable)
print('float variable converted to an int:', int_variable)


# %%% Examples / basic inputs
# From zyBooks 1.2

hours = 40
weeks = 50
hourly_wage = int(input('Enter hourly wage: '))

print('Salary is', hourly_wage * hours * weeks)

human_years = int(input('Enter age of dog (in human years): '))
print()

dog_years = 7 * human_years

print(human_years, 'human years is about', end=' ')
print(dog_years, 'dog years.')

# %%% Examples / float num (1)
# From zyBooks 1.4

miles = float(input('Enter a distance in miles: '))
hours_to_fly = miles / 500.0
hours_to_drive = miles / 60.0

print(miles, 'miles would take:')
print(hours_to_fly, 'hours to fly')
print(hours_to_drive, 'hours to drive')

# %%% Example / float (2)
# Energy to mass convertion
c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9

# Read in a floating-point number from the user
mass_kg = float(input())

# Compute E = mc^2.
energy_joules = mass_kg * (c_meters_per_sec**2)  # E = mc^2
print('Total energy released:', energy_joules, 'Joules')

# Calculate equivalent number of AA and tons of TNT.
num_AA_batteries = energy_joules / joules_per_AA_battery
num_TNT_tons = energy_joules / joules_per_TNT_ton

print('Which is as much energy as:')
print('  ', num_AA_batteries, 'AA batteries')
print('  ', num_TNT_tons, 'tons of TNT')

# %%% Overflow
# Float overflow

print('2.0 to the power of 256 =', 2.0**256)
print('2.0 to the power of 512 = ', 2.0**512)
print('2.0 to the power of 1024 = ', 2.0**1024)

# %% M1: Arithmentic

2 + 1
3 * 2
6 / 2

(2 + 1) + (3 * 9)
(5 * 4) / (3 + 2)

# From zyBooks Ch. 1
x = 4
w = 2

y = 3 * (x + (10 / w))

# Division operator / performs division and returns a floating-point number
20 / 10
50 / 50
5 / 10

# The floored division operator // rounds down the result
20 // 10
50 // 50
5 // 10

# The modulo operator (%) evaluates the remainder of the division
24 % 10
50 % 50
5 % 10


# %%% math library
# https://docs.python.org/3/library/math.html?highlight=math#module-math
#
# needs `import math` above

base = float(input('Enter initial savings: '))
print()

rate = float(input('Enter annual interest % rate: '))
print()

years = int(input('Enter years that pass: '))
print()

total = base * math.pow(1 + (rate / 100), years)

print('Savings after', years, 'years is', total)

help(math)

math.e


# %%% Equality operators

'''
Equality operators 	Description 	Example (assume x is 3)
== 	a == b means a is equal to b 	x == 3 is True
x == 4 is False
!= 	a != b means a is not equal to b 	x != 3 is False
x != 4 is True
'''

user_num = int(input('Enter a number: '))

if user_num == 0:
    print('Zero')
else:
    print('Non-zero')


# %%% Relational operators

'''
Relational operators 	Description 	Example (assume x is 3)
< 	a < b means a is less than b 	x < 4 is true
x < 3 is false
> 	a > b means a is greater than b 	x > 2 is true
x > 3 is false
<= 	a <= b means a is less than or equal to b 	x <= 4 is true
x <= 3 is true
x <= 2 is false
>= 	a >= b means a is greater than or equal to b 	x >= 2 is true
x >= 3 is true
x >= 4 is false
'''

a = 10
b = 20

if a > b:
    print('a is greater than b')
else:
    print('a is less than or equal to b')


# %%% Boolean operators
'''
Boolean operator 	Description
a and b 	Boolean AND: True when both operands are True.
a or b 	Boolean OR: True when at least one operand is True.
not a 	Boolean NOT (opposite): True when the operand is False.
'''

t = True
f = False

andff = f and f
andft = f and t
andtf = t and f
andtt = t and t

orff = f or f
orft = f or t
ortf = t or f
ortt = t or t

nott = not t
notf = not f

xorff = (f and not f) or (not f and f)
xorft = (f and not t) or (not f and t)
xortf = (t and not f) or (not t and f)
xortt = (t and not t) or (not t and t)


# %% M2: If statements

hotel_rate = 155

user_age = int(input('Enter age: '))

# Notice the indentation after the `:` colon in the if statement
if user_age > 65:
    hotel_rate = hotel_rate - 20

print('Your hotel rate:', hotel_rate)

# %%% if else

user_age = int(input('Enter age: '))

if user_age < 25:
    insurance_price = 4800
else:
    insurance_price = 2200

print('Annual price: ${}'.format(insurance_price))

# %%% Multi-branch if

num_years = int(input('Enter number years married: '))

if num_years == 1:
    print('Your first year -- great!')
elif num_years == 10:
    print('A whole decade -- impressive.')
elif num_years == 25:
    print('Your silver anniversary -- enjoy.')
elif num_years == 50:
    print('Your golden anniversary -- amazing.')
else:
    print('Nothing special.')


# %% M3: Loops
# Control constructs
# Based on zyBooks Ch. 3

# %%% While loops
# From zyB Ch. 3.1
# A while loop repeatedly executes an indented block of code
# (known as the loop body) as long as the loop's expression is True.

curr_power = 2
user_char = 'y'

while user_char == 'y':
    print(curr_power)
    curr_power = curr_power * 2
    user_char = input()

print('Done')

# Simple example with += (sorthand for i = i + 1)
i = 0
while i <= 8:
    print(i, end=' ')
    i += 1

# %%% range()
# from zyB Ch. 3.3

# range(start, stop[, step])
# defaults start = 0, step = 1
help(range)

for i in range(3):
    print(i, end=' ')

# %%% For loops
# From zyB Ch. 3 and stackoverflow

# Here is a nice discussion on Python for-loops
# Source:
# https://stackoverflow.com/questions/56040789/how-to-make-a-for-loop-more-understandable-in-python/56041379

for i in range(1, 11):
    print(i)

# It can also be written as follows (code source stackoverflow)
start = 1
length = 10
for i in range(start, start + length):
    print(i)

x = 0
while x < 10:
    print(x)
    x += 1

i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # range(10)
for x in i:
    print(i)
    print(x)     # note, stackoverflow answer only had print(i)

# The following examples came from zyBooks

names = ['Janice', 'Clarice', 'Martin', 'Veronica', 'Jason']

num = int(input('Enter number of names to print: '))
for i in range(len(names)):
    if i == num:
        break
    print(names[i], end=' ')
else:
    print('All names printed.')

origins = [4, 8, 10]

for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Element {}: {}'.format(index, value))

origins = [4, 8, 10]

for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print('Element {}: {}'.format(index, value))

# The enumerate() function retrieves both the index and corresponding
# element value at the same time
origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print('Element {}: {}'.format(index, value))

channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))

my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)

daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: ${:.2f}'.format(total))
print('Daily average revenue: ${:.2f}'.format(average))

names = [
    'Biffle',
    'Bowyer',
    'Busch',
    'Gordon',
    'Patrick'
]

i = 0
for name in names:
    print(name, '|', end=' ')
    print(i)
    i += 1

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')

# %% M4: Functions
# import filename as something -- do not enter filename.py, just filename
# import my_vignette_library as my

# %%% ftn w/o arg, w/o return
#
# Functions with no arguments and do not return anything
#
my.hello_world()
my.goodbye_cruel_world()
my.hello_goodbye()

# %%% ftn with args, w/o return
#

# Takes two arguments, numeric or strig
my.args2_noreturn(100, 200)
my.args2_noreturn("a", "b")

# Takes 2 numbers and adds them. No return
a = 12
b = 14
my.add_2_nums_noreturn(a, b)

# How about sending a list (a special kind, called tuple)
L = (2, 3, 5)
type(L)
my.args2_noreturn(L, "hello, tuple")


# %%% ftn with args, with return
#
# Takes 2 numbers and adds them, and get a return
a = 5
b = 3
c = my.add_2_nums_withreturn(a, b)
print(c)

# Takes one argument and returns one argument
a = my.get_cube(5)
print(a)

# %%% ftn with args and multiple return
#
# Takes one argument and returns two arguments
my.get_square_and_cube(2)

# %%% ftn with optional argument
# Takes two arguments, but one has a default, and returns one argument
a = my.power_x_to_the_y(2)
print(a)

# You can override the default value of the optional argument
a = my.power_x_to_the_y(2, 8)
print(a)

# You can override the default value of the optional argument
my.power_x_to_the_y(2, 8)

# Now you have 1 regular argument and 2 optional arguments
# Override one of the optional args, and take a default value
my.power_x_to_the_y_plus_z(2, 8)

# Override the default of both of the optional arguments
my.power_x_to_the_y_plus_z(2, 8, 500)

# We can change the order of the optional argument because they have key names
my.power_x_to_the_y_plus_z(2, z=500, y=8)

# %%% ftn special list of *args
#
# Send 4 arguments (4 numbers)
v = my.sum_various_numbers(4, 5, 10, 4)
print(v)

# Now send 7 arguments to the same functions (7 numbers)
my.sum_various_numbers(1, 2, 3, 5, 7, 11)

# Or send 3 numbers to the same functions
my.sum_various_numbers(2, 4, 6)

my.multiply_the_sum_of_various_numbers(100, 2, 4, 6)

# %%% ftn with **kwargs

my.take_various_kewordvars(name="Jake", lastname="Blues")

d = my.take_various_kewordvars(name="Jojo", city="Tucson", state="Arizona")

d.items()

# %% M5: Data Structures

# %%% Lists
# From zyB Ch. 2.31
# A container is a construct used to group related values together and
# contains references to other objects instead of data.

'''
List operations
len(list)
   Find the length of the list.
list1 + list2
   Produce a new list by concatenating list2 to the end of list1.
min(list)
   Find the element in list with the smallest value.
max(list)
   Find the element in list with the largest value.
sum(list)
   Find the sum of all elements of a list (numbers only).
list.index(val)
   Find the index of the first element in list whose value matches val.
list.count(val)
   Count the number of occurrences of the value val in list.
'''

# Some of the most expensive cars in the world
lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

# Create a simple list based on that data
prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

# Lists are indexed, starting with 0
print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')

# Modify list elements
my_nums = [5, 12, 20]
print(my_nums)

# Modify a list element
my_nums[1] = -28
print(my_nums)

# Adding and removing list elements
my_list = [10, 'bw']
print(my_list)

my_list.append('abc')
print('After append:', my_list)

my_list.pop(1)
print('After pop:', my_list)

my_list.remove('abc')
print('After remove:', my_list)

# Concatenating lists
# Concatenating lists
house_prices = [380000, 900000, 875000] + [225000]
print('There are', len(house_prices), 'prices in the list.')

# Finding min, max
print('Cheapest house:', min(house_prices))
print('Most expensive house:', max(house_prices))

# %%% List operations
'''
From zyBook table 5.1.1

Operation 	Description 	Example code 	Example output

my_list = [1, 2, 3] 	Creates a list.
    my_list = [1, 2, 3]
    print(my_list)
    [1, 2, 3]

list(iter) 	Creates a list.
    my_list = list('123')
    print(my_list)
    ['1', '2', '3']

my_list[index] 	Get an element from a list.
    my_list = [1, 2, 3]
    print(my_list[1])
    2

my_list[start:end] 	Get a new list containing some of another list's elements.
    my_list = [1, 2, 3]
    print(my_list[1:3])
    [2, 3]

my_list1 + my_list2 	New list with my_list2 added to end of my_list1.
    my_list = [1, 2] + [3]
    print(my_list)
    [1, 2, 3]

my_list[i] = x 	Change the value of the ith element in-place.
    my_list = [1, 2, 3]
    my_list[2] = 9
    print(my_list)
    [1, 2, 9]

my_list[len(my_list):] = [x] 	Add the elements in [x] to the end of my_list.
                               The append(x) method (explained above
                               section) may be preferred for clarity.
    my_list = [1, 2, 3]
    my_list[len(my_list):] = [9]
    print(my_list)
    [1, 2, 3, 9]

del my_list[i] 	Delete an element from a list.
    my_list = [1, 2, 3]
    del my_list[1]
    print(my_list)
    [1, 3]
'''

'''
Adding elements
list.append(x) 	Add an item to the end of list.
    my_list = [5, 8]
    my_list.append(16)
    [5, 8, 16]

list.extend([x]) 	Add all items in [x] to list.
    my_list = [5, 8]
    my_list.extend([4, 12])
    [5, 8, 4, 12]

list.insert(i, x) 	Insert x into list before position i.
    my_list = [5, 8]
    my_list.insert(1, 1.7)
    [5, 1.7, 8]
'''

'''
Removing elements
list.remove(x) 	Remove first item from list with value x.
    my_list = [5, 8, 14]
    my_list.remove(8)
    [5, 14]

list.pop() 	Remove and return last item in list.
    my_list = [5, 8, 14]
    val = my_list.pop()
    [5, 8]
    val is 14

list.pop(i) 	Remove and return item at position i in list.
    my_list = [5, 8, 14]
    val = my_list.pop(0)
    [8, 14]
    val is 5
'''

'''
Modifying elements
list.sort() 	Sort the items of list in-place.
    my_list = [14, 5, 8]
    my_list.sort()
    [5, 8, 14]

list.reverse() 	Reverse the elements of list in-place.
    my_list = [14, 5, 8]
    my_list.reverse()
    [8, 5, 14]
'''

'''
Miscellaneous
list.index(x) 	Return index of first item in list with value x.
my_list = [5, 8, 14]
print(my_list.index(14))
Prints "2"

list.count(x) 	Count the number of times value x is in list.
my_list = [5, 8, 5, 5, 14]
print(my_list.count(5))
Prints "3"
'''

# %%% Iterating a list
# From zyBooks Ch. 5.3

'''
Function 	Description 	Example code 	Example output
all(list) 	True if every element in list is True (!= 0),
            or if the list is empty.
    print(all([1, 2, 3]))
    print(all([0, 1, 2]))
    True
    False

any(list) 	True if any element in the list is True.
    print(any([0, 2]))
    print(any([0, 0]))
    True
    False

max(list) 	Get the maximum element in the list.
    print(max([-3, 5, 25]))
    25

min(list) 	Get the minimum element in the list.
    print(min([-3, 5, 25]))
    -3

sum(list) 	Get the sum of all elements in the list.
    print(sum([-3, 5, 25]))
    27
'''

# Example 1
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('{}: {}'.format(index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num is None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num is not None) and (num > max_num) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)

# Example 2
nums = [1, 4, 15, 456]

max_even = None
for num in nums:
    if num % 2 == 0:    # The number is even?
        if max_even is None or num > max_even:  # Greatest even number seen?
            max_even = num

# %%% List slicing
'''
A programmer can use slice notation to read multiple elements from a list,
creating a new list that contains only the desired elements.
The programmer indicates the start and end positions of
a range of elements to retrieve, as in my_list[0:2].
'''

'''
Operation 	Description 	Example code 	Example output
my_list[start:end] 	Get a list from start to end (minus 1).
    my_list = [5, 10, 20]
    print(my_list[0:2])
    [5, 10]

my_list[start:end:stride] 	Get a list of every stride element
                           from start to end (minus 1).
    my_list = [5, 10, 20, 40, 80]
    print(my_list[0:5:3])
    [5, 40]

my_list[start:] 	Get a list from start to end of the list.
    my_list = [5, 10, 20, 40, 80]
    print(my_list[2:])
    [20, 40, 80]

my_list[:end] 	Get a list from beginning of list to end (minus 1).
    my_list = [5, 10, 20, 40, 80]
    print(my_list[:4])
    [5, 10, 20, 40]

my_list[:] 	Get a copy of the list.
    my_list = [5, 10, 20, 40, 80]
    print(my_list[:])
    [5, 10, 20, 40, 80]'
'''

boston_bruins = ['Tyler', 'Zdeno', 'Patrice']
print('Elements 0 and 1:', boston_bruins[0:2])
print('Elements 1 and 2:', boston_bruins[1:3])

my_list = ['practicing', 'with', 'list', 'slicing']
print(my_list[0:3])
print(my_list[1:2])

election_years = [1992, 1996, 2000, 2004, 2008]
print(election_years[0:-1])  # Every year except the last
print(election_years[0:-3])  # Every year except the last three
print(election_years[-3:-1])  # The third and second to last years



# %%% Tuples
# ...cont. ch 2.31
# A tuple behaves similar to a list but is immutable
# – once created the tuple's elements cannot be changed.
# Build tuples using parenthese ()

# Examples
white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

# Error. Tuples are immutable
white_house_coordinates[1] = 50

# Needs namedtuple package
# from collections import namedtuple

# Create named tuple
Car = namedtuple('Car', ['make', 'model', 'price', 'horsepower', 'seats'])

# Use the named tuple to describe a car
chevy_blazer = Car('Chevrolet', 'Blazer', 32000, 275, 8)

# Use the named tuple to describe a different car
chevy_impala = Car('Chevrolet', 'Impala', 37495, 305, 5)

print(chevy_blazer)
print(chevy_impala)

# %%% Dictionaries
# From zyB Ch 2.29.
# "A dictionary is a Python container used to describe associative
# relationships."
# { keys : values }

# Table 5.5.1
'''
my_dict[key] 	Indexing operation – retrieves the value associated with key.
    jose_grade = my_dict['Jose']

my_dict[key] = value 	Adds an entry if the entry does not exist,
                        else modifies the existing entry.
    my_dict['Jose'] = 'B+'

del my_dict[key] 	Deletes the key entry from a dict.
del my_dict['Jose']

key in my_dict 	Tests for existence of key in my_dict.
    if 'Jose' in my_dict: # ...
'''

players = {
    'Lionel Messi': 10,
    'Cristiano Ronaldo': 7
}

print(players)

# it is a dict object
type(players)

caffeine_content_mg = {
    'Mr. Goodbar chocolate': 122,
    'Red Bull': 33,
    'Monster Hitman Sniper energy drink': 270,
    'Lipton Brisk iced tea - lemon flavor': 2,
    'dark chocolate coated coffee beans': 869,
    'Regular drip or percolated coffee': 60,
    'Buzz Bites Chocolate Chews': 1639
}

print(caffeine_content_mg)

prices = {}  # Create empty dictionary

prices = {'apples': 1.99, 'oranges': 1.49}

# Accessing disct entries (values) for each key

print('The price of apples is', prices['apples'])
print('\nThe price of lemons is', prices['lemons'])

# Adding keys : values to a dictionary
prices['banana'] = 1.49

print(prices)

# Midify an entry
prices['banana'] = 1.69
print(prices)

# Remove and entry
del prices['banana']
print(prices)


# %%% Sets
# From zyB Ch. 2.30
# A set is an unordered collection of unique elements.
# Elements are unordered: Elements in the set do not have a position or index.
# Elements are unique: No elements in the set share the same value.

'''
len(set)
   Find the length (number of elements) of the set.
set1.update(set2)
   Adds the elements in set2 to set1.
set.add(value)
   Adds value into the set.
set.remove(value)
   Removes value from the set.
   Raises KeyError if value is not found.
set.pop()
   Removes a random element from the set.
set.clear()
   Clears all elements from the set.
set.intersection(set_a, set_b, set_c...)
   Returns a new set containing only the elements in common between set
   and all provided sets.
set.union(set_a, set_b, set_c...)
   Returns a new set containing all of the unique elements in all sets.
set.difference(set_a, set_b, set_c...) 	Returns a set containing only the
   elements of set that are not found in any of the provided sets.
set_a.symmetric_difference(set_b)
   Returns a set containing only elements that appear in exactly one
   of set_a or set_b
'''

help(set)

# Create a set using the set() function.
nums1 = set([1, 2, 3])

# Create a set using a set literal.
nums2 = {7, 8, 9}

# Print the contents of the sets.
print(nums1)
print(nums2)

type(nums1)
type(nums2)

# Create sets
names1 = {'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Tia'}

# Add element to set
names1.add('Hyungu')

# Add names2 to names1
names1.update(names2)

# Remove element from set
names1.remove('Dean')

# Clear all elements from set
names2.clear()

# Create sets
names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

# Union names1 and names2
result_set = names1.union(names2)

# Intersection btwn result_set and names3
result_set = result_set.intersection(names3)

# Difference btwn result_set and names4
result_set = result_set.difference(names4)

# %% M6: Libraries

# %%% Standard library

'''
datetime 	Creation and editing of dates and times objects
    https://docs.python.org/3/library/datetime.html
random 	Functions for working with random numbers
    https://docs.python.org/3/library/random.html
copy 	Create complete copies of objects
    https://docs.python.org/3/library/copy.html
time 	Get the current time, convert time zones,
        sleep for a number of seconds
    https://docs.python.org/3/library/time.html
math 	Mathematical functions
    https://docs.python.org/3/library/math.html
os 	Operating system informational and management helpers
    https://docs.python.org/3/library/os.html
sys 	System specific environment or configuration helpers
    https://docs.python.org/3/library/sys.html
pdb 	The Python interactive debugger
    https://docs.python.org/3/library/pdb.html
urllib 	URL handling functions, such as requesting web pages
    https://docs.python.org/3/library/urllib.html
'''

# %%% datetime
# Creation and editing of dates and times objects
# https://docs.python.org/3/library/datetime.html

# import datetime

# Create a new date object representing the current date (May 30, 2016)
today = datetime.date.today()

days_from_now = int(input('Enter number of days from now: '))

# Create a new timedelta object that represents a difference in the
# number of days between dates.
day_difference = datetime.timedelta(days=days_from_now)

# Calculate new date
future_date = today + day_difference

print(days_from_now, 'days from now is', future_date.strftime('%B %d, %Y'))

# %%% random

# import random

# Create a shuffled card deck with 4 suites of cards 2-10, and face cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

num_drawn = 0
game_over = False
user_input = input("Press any key to draw a card ('q' to quit): ")
while user_input != 'q' and not game_over:

    # Draw a random card, and remove card from the deck
    card = random.choice(deck)
    deck.remove(card)
    num_drawn += 1

    print('\nCard drawn:', card)

    # Game is over if an ace was drawn
    if card == 'A':
        game_over = True
    else:
        user_input = input("Press any key to draw a card ('q' to quit): ")

if user_input == 'q':
    print("\nGame was quit")
else:
    print(num_drawn, 'card(s) drawn to find an ace.')

# %%% matplotlib
# http://www.cru.uea.ac.uk/cru/data/temperature/#datdow

# import matplotlib.pyplot as plt

with open('ocean_temps.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

years = range(1850, 2012)

plt.plot(years, temps)
plt.show()

# Multiple lines
# import matplotlib.pyplot as plt

with open('ocean_temp.csv') as temp_file:
    temps = []
    for t in temp_file:
        temps.append(float(t))

temp_years = range(1850, 2012)
plt.plot(temp_years, temps)

pirate_years = range(1850, 2025, 25)
num_pirates_thousands = [20, 17, 15, 5, 0.4, 0.05, 0.025]
plt.plot(pirate_years, num_pirates_thousands)
plt.show()

# %%% numpy
# The numpy package provides tools for scientific and mathematical
# computations in Python.

# import numpy as np

# 1-dimension array
my_array1 = np.array([15.5, 25.11, 19.0])
print('my_array_1:')
print(my_array1)
print()

# 2-dimension array
my_array2 = np.array([(34, 25), (16, 12)])
print('my_array_2:')
print(my_array2)

zero_array = np.zeros((1, 5))   # Single dimension array with 5 elements
print('zero_array:')
print(zero_array)
print()

# 5-dimension array with 2 elements in each dimension.
one_array = np.ones((5, 2))
print('one_array:')
print(one_array)

# The linspace numpy function creates a sequence by segmenting a
# given range with a specified number of points.
print(np.linspace(0, 1, 11))
print()
print(np.linspace(0, np.sin(np.pi / 4), 20))

# Mathematical operations between arrays are performed between
# the matching elements of each array.
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

print('Adding arrays (array1 + array2)')
print(array1 + array2)

print('\nSubtracting arrays (array1 - array2)')
print(array1 - array2)

print('\nMultiplying arrays (array1 * array2)')
print(array1 * array2)

print('\nMatrix multiply (dot(array1 * array2))')
print(np.dot(array1, array2))

print('\nFinding square root of each element in array1')
print(np.sqrt(array1))

print('\nFinding minimum element in array1')
print(array1.min())

print('\nFinding maximum element in array1')
print(array1.max())


# %% References
"""
Tips and references:

runfile('functions_intro.py')

# Delete all variables from the namespace
%reset
help(functioname)

References:
* zyBooks for CEIS110
* The Python Tutorial, https://docs.python.org/3/tutorial/
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    https://docs.python.org/3/tutorial/datastructures.html
* https://numpy.org/doc/stable/reference/generated/numpy.array.html
* VanderPlas, J. "Python Data Science Handbook", O'Reilly Media 2016
* VanderPlas, J. "A Whirlwind Tour of Python" O'Reilly Media 2016
"""

