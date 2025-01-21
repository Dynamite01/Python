import random



def calculate_gpa(grades):
    # Step 1: Check if there are exactly 7 grades
    if len(grades) != 7:
        return "Error: You must provide grades for all 7 courses"

    # Step 2: Validate each grade
    for i in grades:
        try:
            float(i)
            if i < 0 and i > 100:
                return f"Error: {i} is not between 0 and 100"
        except:
            return f"Error: {i} is not a valid number"

    # Step 3: Initialize variables for GPA calculation
    total_points = 0
    credits = 5

    # Step 4: Calculate GPA points for each grade
    for i in grades:
        temp = 0
        if 95 <= i <= 100:
            temp = 4.0
        elif 90 <= i <= 94:
            temp = 3.67
        elif 85 <= i <= 89:
            temp = 3.33
        elif 80 <= i <= 84:
            temp = 3.0
        elif 75 <= i <= 79:
            temp = 2.67
        elif 70 <= i <= 74:
            temp = 2.33
        elif 65 <= i <= 69:
            temp = 2.0
        elif 60 <= i <= 64:
            temp = 1.67
        elif 55 <= i <= 59:
            temp = 1.33
        elif 50 <= i <= 54:
            temp = 1.0
        elif 0 <= i <= 49:
            temp = 0.0
        total_points+=(temp*5)

    # Step 5: Calculate final GPA
    total_credits = len(grades) * credits
    gpa = round((total_points/total_credits), 2)

    return gpa

def calculate_class_gpa(class_data):
    avg_gpa = 0.0
    # Step 1: Calculate individual GPAs
    for i in class_data:
        avg_gpa += calculate_gpa(class_data[i])
        print(calculate_gpa(class_data[i]))


    # Step 2: Calculate average of GPAs
    # TODO: Sum all GPAs and divide by number of students
    avg_gpa /= len(class_data)
    print(len(class_data))

    return avg_gpa

def is_valid_password(password):
    # Lists of valid characters
    UPPERCASE_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    LOWERCASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    SPECIAL_CHARS = ['!', '@', '?']


    is_len = False
    is_upper = False
    is_lower = False
    is_nums = False
    is_special = False
    # TODO: Check password length (minimum 8 characters)
    if len(password) >= 8:
        is_len = True

    # TODO: Check for at least one uppercase letter
    for i in password:
        if i in UPPERCASE_CHARS:
            is_upper = True
            break

    # TODO: Check for at least one lowercase letter
    for i in password:
        if i in LOWERCASE_CHARS:
            is_lower = True
            break

    # TODO: Check for at least one number
    for i in password:
        if i in NUMBERS:
            is_nums = True
            break

    # TODO: Check for at least one special character
    for i in password:
        if i in SPECIAL_CHARS:
            is_special = True
            break

    return is_special and is_nums and is_upper and is_lower and is_len

def play_rpsls(user_choice):
    # Game choices
    CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    if user_choice not in CHOICES:
        return """Invalid choice!
                  Valid choices are: rock, paper, scissors, lizard, spock"""

    computer_choice = random.choice(CHOICES)

    WINNING_RULES = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # Determine the winner
    if user_choice == computer_choice:
        result =f"""You chose: {user_choice}
Computer chose: {computer_choice}
It's a tie!"""

    elif computer_choice in WINNING_RULES[user_choice]:
        result = f"""You chose: {user_choice}
Computer chose: {computer_choice}
Result: You win!"""
    else:
        result = f"""You chose: {user_choice}
Computer chose: {computer_choice}
Result: You lose!"""

    # Print the result
    return result

def calculate_age(birth_date_str):
    # Dictionary of days in each month (non-leap year)
    DAYS_IN_MONTH = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }

    # Dictionary to convert month names to numbers
    MONTHS = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }

    current_year = 2024
    current_month = 1
    current_day = 6

    # Step 1: Parse the birth date string
    birth_date = birth_date_str.split()
    birth_date[1] = MONTHS[birth_date[1].lower()]
    if len(birth_date[0]) == 4:
        birth_date = [int(birth_date[2]), int(birth_date[1]), int(birth_date[0])]
    else:
        birth_date = [int(birth_date[0]), int(birth_date[1]), int(birth_date[2])]

    birth_day, birth_month, birth_year = birth_date

    # Step 2: Check if a year is a leap year
    def is_leap(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    # Step 3: Calculate years, months, and days
    age_years = current_year - birth_year
    age_months = current_month - birth_month
    age_days = current_day - birth_day

    # Step 4: Adjust for negative days
    if age_days < 0:
        if current_month == 1:
            previous_month = 12
            previous_year = current_year - 1
        else:
            previous_month = current_month - 1
            previous_year = current_year

        days_in_previous_month = DAYS_IN_MONTH[previous_month]
        if previous_month == 2 and is_leap(previous_year):
            days_in_previous_month += 1

        age_days += days_in_previous_month
        age_months -= 1

    # Step 5: Adjust for negative months
    if age_months < 0:
        age_months += 12
        age_years -= 1

    # Step 6: Return the formatted string
    return f"You are {age_years} years, {age_months} months, and {age_days} days old."





