#task10
the_number = int(input("Enter a number: "))  #for number
number  = 1  # initializing the number
factorial = 1  # initializing the factorial


while (number <= the_number):
    factorial  *= number  # calculating the factorial of the number
    number += 1  # loop to print the numbers from 1 to the user's

print(f"The factorial of {the_number} is  {factorial}")  # printing the factorial of the number
    