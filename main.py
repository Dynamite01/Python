#task1: Input and Prints
name = str(input("Enter your name: "))     #for name 
fav_lang = str(input("Enter your favourite programming language: "))   #for favourite programming language

print(f'Hello', {name}, 'you love', {fav_lang}) # printing the output

#task2: Input and Prints
first_num = int(input("Enter the first number  number: "))   #for first number
seconde_num = int(input("Enter the second number number: ")) #for second number

sum_result = first_num + seconde_num   # calculating sum of two numbers
diff_result = first_num - seconde_num  # calculating difference of two numbers  

print(f'Sum of the two numbers:', {sum_result})  # printing the sum of two numbers
print(f'Difference of the two numbers:', {diff_result})  # printing the difference of two numbers

#task3:Numbers and Arithmetic Operations

length = int(input("Enter the length of the rectangle: "))  #for length of the rectangle
width = int(input("Enter the width of the rectangle: "))  #for width of the rectangle

area = length * width  # calculating area of the rectangle     
print(f'The area of the rectangle is :', {area})  # printing the area of the rectangle

#task4:Numbers and Arithmetic Operations

number = int(input("Enter the number: "))  #for number
if(number % 3 == 0 and number % 5 == 0):  # checking if the number is divisible by both 3 and 5
    print({number},f'is divisible by 3 and 5' )
else: # if the number is not divisible by both 3 and 5
    print( [number],f'is not divisible by 3 and 5' )

#task5:Strings and Lists
sentence = str(input("Enter a sentence: "))  #for lowercase word
uppercased__word = sentence.upper()  # converting the sentence to uppercase
word_count = len(sentence.split())  # counting the number of words in the sentence
print(f"The sentence in uppercase: ", {uppercased__word})  # printing the sentence in uppercase
print(f"Number of words: ", {word_count})  # printing the length of the sentence


#task6:Strings and Lists
favourite_fruits =[]  # creating an empty list

for i in range(1,6):  # Loop to collect 5 favorite fruits from the user
    fruit = input(f"Enter your favorite fruit {i}: ")
    favourite_fruits.append(fruit)  # adding the fruit to the list

print('Your favourite fruits are:', favourite_fruits[::-1])  # printing the list of favourite fruits

#task7:Conditionals
user_age = int(input(f"Enter your ege: ")) #the age of the user
if (user_age >= 18): #check if the user is above 18 
    print("You are  eligible to vote. ")
else:
    print("You are not eligible to vote. ") #if the user is below 18 years old

#task8:Conditionals
checking_number = int(input("Enter a number: "))  #for number
if (checking_number < 0):  # checking if the number is negative
    print("The number " , checking_number , " is negative.")
elif(checking_number > 0):  # checking if the number is positive
    print("The number " , checking_number , " is positive.")
else:
    print("The number " , checking_number , " is zero.")  # if the number is zero


#task9:Loops
user_input = int(input("Enter a number: "))  #for number
number = 1  # initializing the number

while (number <= user_input):
    number += 1  # loop to print the numbers from 1 to the user's
    if (number % 2 == 0):
        print(number, end=" ")  # printing the even numbers
        number += 1  # incrementing the number

print("there is no even number")  # if there is no even number



#task10:Loops
the_number = int(input("Enter a number: "))  #for number
number  = 1  # initializing the number
factorial = 1  # initializing the factorial


while (number <= the_number):
    factorial  *= number  # calculating the factorial of the number
    number += 1  # loop to print the numbers from 1 to the user's

print(f"The factorial of {the_number} is  {factorial}")  # printing the factorial of the number



