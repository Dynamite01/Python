# Курсовая система регистрации

# Инициализация словаря курсов
courses = {
    "CS101": ("Введение в информатику", "Доктор Смит", 30, set()),
    "MATH203": ("Математика II", "Доктор Джонсон", 25, set()),
    "PHY150": ("Общая физика", "Доктор Кларк", 20, set()),
    "ENG102": ("Английский композит", "Доктор Тейлор", 40, set()),
    "BIO110": ("Введение в биологию", "Доктор Ли", 35, set())
}

# Множество регистрированных курсов
registered_courses = set()

# Главное меню
while True:
    print("\nДобро пожаловать в систему регистрации курсов!")
    print("1. Посмотреть все курсы")
    print("2. Зарегистрироваться на курс")
    print("3. Отменить регистрацию на курс")
    print("4. Посмотреть свои курсы")
    print("5. Выход")

    choice = input("\nВыберите опцию: ")

    if choice == "1":
        print("\nДоступные курсы:")
        for code, details in courses.items():
            title, instructor, capacity, enrolled = details
            print(f"\nКод курса: {code}\nНазвание: {title}\nПреподаватель: {instructor}\nВместимость: {capacity}\nЗарегистрировано: {len(enrolled)}")

    elif choice == "2":
        course_code = input("\nВведите код курса: ")
        if course_code in courses:
            title, instructor, capacity, enrolled = courses[course_code]
            if len(enrolled) < capacity:
                if course_code not in registered_courses:
                    enrolled.add("student")  # Замещаем "student" именем текущего пользователя при необходимости
                    registered_courses.add(course_code)
                    print(f"\nВы успешно зарегистрировались на {course_code}: {title}.")
                else:
                    print("\nВы уже регистрированы на этот курс.")
            else:
                print("\nКурс уже заполнен.")
        else:
            print("\nКурс с данным кодом не существует.")

    elif choice == "3":
        course_code = input("\nВведите код курса: ")
        if course_code in registered_courses:
            courses[course_code][3].remove("student")
            registered_courses.remove(course_code)
            print(f"\nВы успешно сняли регистрацию с {course_code}.")
        else:
            print("\nВы не зарегистрированы на этот курс.")

    elif choice == "4":
        if registered_courses:
            print("\nВы зарегистрированы на следующие курсы:")
            for course_code in registered_courses:
                title = courses[course_code][0]
                print(f"- {course_code}: {title}")
        else:
            print("\nВы не зарегистрированы ни на один курс.")

    elif choice == "5":
        print("\nСпасибо за использование системы регистрации курсов. \u0414о свидания!")
        break

    else:
        print("\nНеверный ввод. Пожалуйста, выберите опцию от 1 до 5.")
