##################################
# Matthew Ryan Buchanan
# set 3a
##################################


#1 Find numbers divisible by 7 and multiple of 5 in a range
lst = []
for x in range(1500, 2701):
    if ( (x % 7 == 0) and (x % 5 == 0) ):
        lst.append(x)
print(lst)


#2 Function to convert between celcius and fahreheit with input in float or int
import math
def temp_converter():
    temp_scale = input("Enter c to convert from celcius to fahrenheit, or f to convert from fahrenheit to celcius")
    temp_input = float(input("Enter the temparature to conver"))
    if temp_scale == 'c':
        print(str(temp_input) + '\u00b0' + "C is " + str(math.floor(temp_input * (9.0/5.0) + 32)) + '\u00b0' + " in Fahrenheit")
    elif temp_scale == 'f':
        print(str(temp_input) + '\u00b0' + "F is " +  str(math.floor((temp_input - 32) * (5.0/9.0))) + '\u00b0' + " in Celsius")

temp_converter()


#3 Function to ask user to guess a number between 1 and 9 inclusive
import random
def num_guess_game():
    rand_num = random.randrange(1,9)
    guess = 0
    while guess != rand_num:
        guess = int(input("Guess the number between 1 and 9"))
    print("Well guessed!")

num_guess_game()


#4 and #5 display a pattern using nested for loop
lines = 9
for i in range(1,10) :
    l = []
    if(i <= 5):
        for j in range(1,i + 1):
            l.append("* ")
    else:
        for k in range(1, 11 - i):
            l.append("* ")
    tmp = ""
    for n in l:
        tmp += n
    print(tmp)


#6 Function to reverse an input from user
def rev_word():
    w = input("Please enter the word to reverse")
    print(w[::-1])

rev_word()


#7 Function to count even and odd numbers in a series of input numbers
def count_odd_even(l):
    even_count = 0
    for n in l :
        if n % 2 == 0:
            even_count = even_count + 1
    print("Number of even numbers: " + str(even_count))
    print("Number of odd numbers: " + str(len(l) - even_count))

sample_input = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd_even(sample_input)


#8 Function to print each item and its type from a list
def item_and_type(l):
    for i in l:
        print("item: " + str(i) + " type: " + str(type(i)))

sample_lst = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
item_and_type(sample_lst)


#9 Print all numbers from 0 to 6 except 3 and 6
for n in range(0,7):
    if n == 3 or n == 6:
        continue
    print(n)