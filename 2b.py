############################
# Matthew Ryan Buchanan
# 2.b excluding ones with solution given
############################




#1
lst = [1, "word", 3.4]
for item in lst:
    print(item)


#2
lst = [1,1,[1,2]]
print(lst[2][1])


#3
lst = ['a','b','c']
print(lst[1:])


#4
weekdays = {'Monday' : 0, 'Tuesday' : 1, 'Wednsday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}
print(weekdays['Tuesday'])


#5
d = {'k1' : [1,2,3]}
print(d['k1'][1])


#6
t = ([1,[2,3]])
print(t[0])
t[0] = 3
print(t[0])
# So mutable objects placed inside a tuple remain mutable once inside the tuple?
# Does the tuple just contain a reference to the list? And the reference is immutable?


#7
# Turn Mississippi into a set and return only unique letters
def ol_miss():
    return set("Mississippi")



#8
tmp = ol_miss()
tmp.add('X')
print(tmp)
# Yes you can add elements not already in a set to a set


#9
print(set([1,1,2,3]))
# sets only contain unique elements


#Question 1
lst = []
for x in range(2000, 3201):
    if ( (x % 7 == 0) and (x % 5 != 0) ):
        lst.append(x)
print(lst)


#Question 2 iterative solution
def factorial_iterative(input_num):
    if input_num == 0:
        return 1
    tmp_num = 1
    for x in range(1, input_num + 1):
        tmp_num *= x
    return tmp_num
print(factorial_iterative(int(input("Please input the number to factorial:"))))

# recursive approach
def factorial_recursive(input_num):
    if input_num == 0:
        return 1
    return input_num * factorial_recursive(input_num - 1)
print(factorial_recursive(int(input("Please input the number to factorial"))))


# The solutions for the rest of the problems are present. Were we just supposed to copy these?