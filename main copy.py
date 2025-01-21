import random
# Task 1: Calculate GPA
# Entering the percentage of grades for each course
def calculate_gpa(grades):
    if len(grades) != 7:  # testing to values of scores
        return "Error: Exactly 7 grades are required."
    
    for grade in grades:
        if not isinstance(grade, (int, float)) or not (0 <= grade <= 100):
            return f"Error: {grade} is not between 0 and 100"
    
    total_points = 0
    credits = 5  # every discipline has 5 credits
    for grade in grades:
        if grade >= 90:
            points = 4.0
        elif grade >= 80:
            points = 3.0
        elif grade >= 70:
            points = 2.0
        elif grade >= 60:
            points = 1.0
        else:
            points = 0.0
        total_points += points * credits
    
    total_credits = 7 * credits
    gpa = round(total_points / total_credits, 2)
    return gpa



# Task 2: Calculate Class GPA

def calculate_class_gpa(class_data):
    gpas = []
    for student, grades in class_data.items():
        gpa = calculate_gpa(grades)
        if isinstance(gpa, str):  # Error case
            return f"Error for {student}: {gpa}"
        gpas.append(gpa)
    
    avg_gpa = round(sum(gpas) / len(gpas), 2)
    return avg_gpa

# Task 3: Validate Password
def is_valid_password(password):
    # Lists of valid characters
    UPPERCASE_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    LOWERCASE_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    SPECIAL_CHARS = ['!', '@', '?']
    
    # TODO: Check password length (minimum 8 characters)
    if len(password) < 8:
        return False
    
    # Flags for different requirements
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_char = False

    # TODO: Check for at least one uppercase letter
    for i in password:
        if i in UPPERCASE_CHARS:
            has_uppercase = True
    
    
    # TODO: Check for at least one lowercase letter
    for i in password:
        if i in LOWERCASE_CHARS:
           has_lowercase = True
       
    
    # TODO: Check for at least one number
    for i in password:
        if i in NUMBERS:
            has_number = True
    
    # TODO: Check for at least one special character
    for i in password:
        if i in SPECIAL_CHARS:
            has_special_char = True
    
    
    # TODO: Check for at least one special character
    for i in password:
        if i in SPECIAL_CHARS:
            has_special_char = True
    
    if has_uppercase and has_lowercase and has_number and has_special_char:
            return True
    else:
        return False
    

# Task 4: Rock-Paper-Scissors-Lizard-Spock Game


def play_rpsls(user_choice):
    CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    if user_choice not in CHOICES:
        return f"Invalid choice! Valid choices are: {', '.join(CHOICES)}"

    computer_choice = random.choice(CHOICES)
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    if computer_choice == user_choice:
        result = "It's a tie!"
    elif computer_choice in rules[user_choice]:
        result = "You win!"
    else:
        result = "You lose!"
    
    return f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}"

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

    # Current date
    current_year = 2024
    current_month = 1
    current_day = 7

    # Step 1: Parse the birth date string
    birth_date = birth_date_str.lower().split()
    
    # Convert month name to number
    if birth_date[1] in MONTHS:
        birth_date[1] = MONTHS[birth_date[1]]
    else:
        return "Invalid month name."
    
    # Determine the date format and convert to [day, month, year]
    if len(birth_date[0]) == 4:  # YYYY Month DD
        birth_date = [int(birth_date[2]), int(birth_date[1]), int(birth_date[0])]
    elif len(birth_date[2]) == 4:  # DD Month YYYY
        birth_date = [int(birth_date[0]), int(birth_date[1]), int(birth_date[2])]
    else:
        return "Invalid date format."

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
        previous_month = current_month - 1 if current_month > 1 else 12
        previous_year = current_year if current_month > 1 else current_year - 1
        
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




