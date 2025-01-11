def view_courses(courses_data: list) -> None:

    print("\nMavjud Kurs:")
    for kurs in range(len(courses_data)):
        print("{}. {} (Duration: {}, Instructor: {})".format(kurs + 1,courses_data[kurs]['course_name'], courses_data[kurs]["duration"], courses_data[kurs]["instructor"]))