# dictionsry with all courses and with codes
courses = {
    "CS101": {
        "title": "Intro to Computer Science",
        "instructor": "Dr. Smith",
        "places": 30,
        "enrolled": set()
    },
    "MATH203": {
        "title": "Calculus II",
        "instructor": "Dr. Johnson",
        "places": 25,
        "enrolled": set()
    },
    "PHY150": {
        "title": "General Physics",
        "instructor": "Dr. Clark",
        "places": 20,
        "enrolled": set()
    },
    "ENG102": {
        "title": "English Composition",
        "instructor": "Dr. Taylor",
        "places": 40,
        "enrolled": set()
    },
    "BIO110": {
        "title": "Introduction to Biology",
        "instructor": "Dr. Lee",
        "places": 35,
        "enrolled": set()
    }
}

registered_courses = set()

def display_courses():
    # to show the all available courses
    print("\nAvailable Courses:")
    for code, details in courses.items():
        print(f"Course Code: {code}")
        print(f"Title: {details['title']}")
        print(f"Instructor: {details['instructor']}")
        print(f"Capacity: {details['places']}")
        print(f"Enrolled: {len(details['enrolled'])}")
        print("-" * 40)

def register_course():
   # to register for a course without duplicates
    course_code = input("Enter the course code to register: ").strip().upper()
    if course_code == courses:
        details = courses[course_code]
        if len(details['enrolled']) < details['places']:
            if course_code != registered_courses:
                details['enrolled'].add("Student")  
                registered_courses.add(course_code)
                details = details['places']-1
                print(f"Successfully registered for {course_code}: {details['title']}.")
            else:
                print(f"You are already registered for {course_code}.")
        else:
            print(f"Course {course_code} is full.")
    else:
        print("Invalid course code.")

# function to delete a courses
def drop_course():
    """Allows the user to drop a course they are registered for."""
    course_code = input("Enter the course code to drop: ").strip().upper()
    if course_code in registered_courses:
        courses[course_code]['enrolled'].remove("Student")  
        registered_courses.remove(course_code)
        print(f"Successfully dropped {course_code}.")
    else:
        print(f"You are not registered for {course_code}.")

def view_registered_courses():
    """Displays all courses the user is currently registered for."""
    if not registered_courses:
        print("You are not registered for any courses.")
    else:
        print("You are registered for the following courses:")
        for course_code in registered_courses:
            title = courses[course_code]['title']
            print(f"- {course_code}: {title}")


    # to show the main menu for the courses and choses
while True:
        print("\nWelcome to the Course Registration System!")
        print("1. View all courses")
        print("2. Register for a course")
        print("3. Drop a course")
        print("4. View my courses")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_courses()
        elif choice == "2":
            register_course()
        elif choice == "3":
            drop_course()
        elif choice == "4":
            view_registered_courses()
        elif choice == "5":
            print("Thank you for using the Course Registration System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.") # it will show when the code was invalid 

