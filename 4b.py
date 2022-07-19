####################################################################
# Matthew Ryan Buchanan
# book store accounting with lists of lists
####################################################################



#1 Build the sample list of orders
list_of_orders = [[34587, "Learning Python, Mark Lutz", 4, 40.95],
                [98762, "Programming Python, Mark Lutz", 5, 56.80], 
                [77226, "Head First Python, Paul Berry", 3, 32.95],
                [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

#2 Map using Lambda funtion to return tuples like (Order Number, Price Per Item * Quantity Ordered) increasing the cost be 10 if value of order is < 100.00, input is the list of orders
answer = map(lambda sub_lst : (sub_lst[0],sub_lst[2] * sub_lst[3]) if (sub_lst[2] * sub_lst[3] > 100.00) else (sub_lst[0],sub_lst[2] * sub_lst[3] + 10.00), list_of_orders)
print(list(answer))


#3 Build sample list of orders in different format
list_of_orders = [[34587, ("Learning Python, Mark Lutz", 4, 40.95), ("Programming Python, Mark Lutz", 2, 56.80)], 
                [98762, ("Programming Python, Mark Lutz", 6, 56.80)], 
                [77226, ("Head First Python, Paul Berry", 3, 32.95), ("Learning Python, Mark Lutz", 2, 40.95), ("Programming Python, Mark Lutz", 3, 56.80)], 
                [88112, ("Einfuhrung in Python3, Bernd Klein", 3, 24.99)]]

# A helper function to process each sublist to return the cost of each order
def list_of_list_helper(l):
    total_price = 0.0
    for item in range(1,len(l)) :
        total_price += l[item][1] * l[item][2]
    return total_price

# Map using lambda funtion to return tuples of form (order number, total price of order)
answer = map(lambda sub_lst : (sub_lst[0], list_of_list_helper(sub_lst)), list_of_orders)
print(list(answer))



