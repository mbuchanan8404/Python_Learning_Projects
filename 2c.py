##############################
# Matthew Ryan Buchanan
# set 2c
##############################


######################
def lst_size_test(l) :
    if len(l) > 3 :
        print("Three's company, four's a crowd!")

lst_of_names = ["Matt", "Mike", "Mary", "Mort"]

lst_size_test(lst_of_names)

lst_of_names.pop()
lst_of_names.remove("Mike")

lst_size_test(lst_of_names)


########################
def lst_size_test_2(l) :
    if len(l) > 3 :
        print("Three's company, four's a crowd!")
    else :
        print("Not too crowded in here at all.")

lst_of_names = ["Matt", "Mike", "Mary", "Mort"]

lst_size_test_2(lst_of_names)

lst_of_names.pop()
lst_of_names.remove("Mike")

lst_size_test_2(lst_of_names)


#####################
def six_is_a_mob(l) :
    if len(l) > 5 :
        print("Its a regular mob in here!")
    elif len(l) <= 5 and len(l) >= 3 :
        print("It's getting a bit crowded in here...")
    elif len(l) == 1 or len(l) == 2 :
        print("Not too crowded, nice!")
    else :
        print("Room is empty.")

lst_of_names = ["Matt", "Mike", "Mary", "Mort", "Mark", "Megan"]

six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)
lst_of_names.pop()
six_is_a_mob(lst_of_names)


