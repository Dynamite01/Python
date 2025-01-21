fruits = ['apple', 'orange', 'banana', ]
quantity = [5, 3, 2]

fruits_zipping = zip(fruits, quantity)
print(fruits_zipping) ## it will not show the correct numbers and elements

# to show correct output we need to make it list    

fruit_qtys_dict = dict(fruits_zipping) #in dictionary we can use only two arguments

fruit_qtys_list = list(fruits_zipping)
print(fruit_qtys_list)
print(fruit_qtys_dict)