from school import students, courses, grades
import pprint
def main():
   
    # talabalarni ma`lumotlarini olish un bo`sh dictionary yaratib oldim
    student = {}

    # Talabalarni saqlash un ustoz bizga tayyor qilib list yaratibdilar👍
    students_data = []
    
    # kurslar ro`yxati
    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]

    # baholar uchun list
    grades_data = []

    while True:
        print("\n=== On-Schoolga Xush Kelibsiz ===","1. Ro'yhatdan o'tish","2. Tizimga kirish","3. Chiqish", sep="\n")
        choose_commond = int(input("Select an option: "))
        
        # agar foydalanuvchi 1 ni tanlasa ro`yxatdan o`tishga o`tadi
        if choose_commond == 1:
            new_student = students.register_student(student, students_data)

            # yangi talabani bazaga qo`shamiz
            students_data.append(new_student)

            print("Muvafaqqiyatli ro'yhatdan o'tildi Xush kelibsiz {}".format(new_student["name"]), end="\n\n")
        #agar foydalanuvchi 2 ni tanlasa profiliga kiradi 
        elif choose_commond == 2:
            
            # serverdan login va parolni kiritib bazada bor yo`qligini so`raymiz va bor bo`lsa userni qaytaramiz
            user = students.login_student(students_data)
            
            while user:
                
                print("\n--- Bosh menu --- \n 1. Kurslar ro'yhatini ko'rish\n 2. Kursga yoziling\n 3. Mening kurslarim ro'yhati\n 4. Mening baholarim \n 5. Tizimdan chiqish\n 6. Bosh menu")
                
                # buyruqni tanlaymiz
                choose_commond_user = int(input("Variant tanglang !!!: "))

                if choose_commond_user == 1:
                    courses.view_courses(courses_data)
                
                elif choose_commond_user == 2:
                    user['course'].append(students.enroll_in_course(courses_data, students_data, user['pas_log']['log']))
                
                elif choose_commond_user == 3:
                    courses.view_courses(user['course'])
                
                elif choose_commond_user == 4:
                    grades.check_grades(user, grades_data)
                
                elif choose_commond_user == 5:
                    break
                
                elif choose_commond_user == 6:
                    exit()
                else:
                    print("\nSiz mavjud bo'lmagan buyruq berdingiz iltimos qaytadan uruning !!! \n")
                  
        elif choose_commond == 3:
        
            print("Biz bilan qolganingiz uchun raxmat ", "Xayr Salomat bo'ling", sep="\n")
            exit()
        
        else: 
            
            print("Siz mavjud bo'lmagan buyruq berdingiz iltimos qaytadan uruning !!! : ", end="\n\n")

main()

if __name__ == "__main__":
    main()