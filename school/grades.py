def check_grades(
        student_courses: dict, 
        grades_data: list 
        ) -> None:
    """
    Displays the grades for a student if available. If no grades are available for 
    the student, it shows a message indicating so.

    Args:
        grades_data (dict): A dictionary where student emails are keys, and their grades 
                             for each course are stored as values.
        student_email (str): The email of the student whose grades are being checked.
    """
    if len(grades_data) == 0:
        print("My Grades:")
        for course in range(len(student_courses['course'])):
            print(f"{student_courses['course'][course]['course_name']}: Not graded yet")



"""


"""