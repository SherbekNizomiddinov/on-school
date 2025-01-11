from os import system
from school import students, courses, grades

def show_menu(
        menu: list[tuple[int, str]],
        user: dict = {}
    ) -> None:

    print(
        "=== Welcome to Online-School ===" if len(menu) == 3 else f"\n--- Main Menu for {user['name']} ---",
        end="\n\n"
    )
    
    for option in menu:
        print(f'{option[0]}. {option[1]}', end="\n")

def main() -> None:
    """
    Main function that drives the On-School system. It displays the main menu, 
    handles user registration and login, and provides an interface for enrolled students 
    to interact with courses and check grades.
    """
    students_data = {
        100001: {
            'email': 'example@gmail.com',
            'name': 'Ali Valiyev',
            'password': '1234'
        },
        100002: {
            'email': 'bjfkabdsfabds',
            'name': 'jkfbadjsbf',
            'password': '324512345'
        }
    }
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]
    grades_data = {}

    menu = [
        (1, "Register"), (2, "Login"), (3, "Exit")
    ]

    user_menu = [
        (1, "View Available Courses"),
        (2, "Enroll in a Course"),
        (3, "View My Courses"),
        (4, "Check My Grades"),
        (5, "Logout")
    ]

    system('clear')

    while True:
        show_menu(menu)
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            students_data = students.register_student(students_data)
        elif choice == "2":
            user_id = students.login_student(students_data)
            if user_id != -1:
                while True:
                    show_menu(user_menu, user=students_data[user_id])
                    user_choice = input("Choose an option: ")
                    if user_choice == '1':
                        # TODO: kurslar royatini chiqarish
                        pass

if __name__ == "__main__":
    main()
