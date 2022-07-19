#################################
# Matthew Ryan Buchanan
# set 4a
#################################



#1 Function to display "Hello World"
def hello_world():
    print("Hello World!")

hello_world()


#2 Function to take a name and output "Hi my name is <name>"
def func1(name):
    print("Hi my name is " + str(name) + "!")

func1("Matt")


#3 Function to take args x,y,z if z is true return x when z is false return y
def func3(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

func3('hello', 'goodbye', False)
func3('hello', 'goodbye', True)


#4 Function to take args x,y and return x * y
def func4(x,y):
    return x * y

func4(8,7)


#5 Function to take arg a and returns true if even and false if odd
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

is_even(0)


#6 Function to take args x,y and return true if x > y, false if x <= y
def compare_xy(x,y):
    if x > y:
        return True
    else:
        return False

compare_xy(3,2)


#7 Function to take an arbitrary number of args and return their sum
def sum_all_args(*nums):
    return sum(nums)

sum_all_args(1,3,2.1,6)


#8 Function to take an arbitrary number of args and return a list of all even args
def lst_of_evens(*nums):
    return [n for n in nums if n % 2 == 0]

lst_of_evens(0,1,2,3,4,5,6,7,8,9.9)


#9 Function to take a string and return a matching string with uppercase even and lowercase odd letters counting spaces
def even_up_odd_low(str):
    new_string = ''
    for i in range(0, len(str)):
        if i % 2 == 0:
            new_string += str[i].upper()
        else:
            new_string += str[i].lower()
    return new_string

even_up_odd_low("test String")


#10 Function which gives lesser than a given number if both the numbers are even, but returns greater if one or both or odd.
def less_if_even(x,y):
    if x % 2 == 0 and y % 2 == 0:
        if x > y:
            return y
        else:
            return x
    else:
        if x > y:
            return x
        else:
            return y

less_if_even(2,3)


#11 Function to take two strings as args and returns true if both start with the same letter, false if they don't
def do_first_letters_match(str1, str2):
    if str1[0].lower() == str2[0].lower():
        return True
    else:
        return False

do_first_letters_match("cat","Bath") 


#12 Function to take a number and return a number twice as far from 7 on the other side of the number line
def temp_name(n):
    if n == 7:
        return n
    elif n > 7:
        return 7 - 2 * (n - 7)
    elif n < 7:
        return 7 + 2 * (7 - n)

temp_name(6)


#13 Function to capitalize first and fourth character in a string arg
def captialize_first_and_fourth(str):
    new_str = ''
    for i in range(0, len(str)):
        if i == 0 or i == 3:
            new_str += str[i].upper()
        else:
            new_str += str[i]
    return new_str

captialize_first_and_fourth("test String")


