import pprint

def register_student(student: dict[str, dict[str, str]], student_date: list) -> None:

    #student nomli dictionary ga "name" nomli key va unga foydalanuvchi kiritgan name ni kiritdik
    student_name = input("Ismingizni kiriting: ")

    # gmail va password ni alohida o`zgaruvchilarga olib oldik
    student_email = input("Emailingizni kiriting: ")
    student_password = input("Parolingizni kiriting: ")
    
    
    # student nomli dictionary ga pas_log nomli nestted dictionary yaratib oldik passwod va loginni saqlash uchun
    while True:
        count_log = student_email.count('@')
        check_log = student_email.find('@')
        length_pass = len(student_password)
        
        if count_log != 1 or check_log == 0 or check_log == len(student_email) - 1:
            print("Gmailni kiritishda hatolik bor iltimos qaytadan urinib ko'ring \n'@' belgisi qo'yilmagan \nyoki boshida va ohirida qo'yilgan bo'lishi mumkin") 
            student_email = input("Enter your email: ")
            
        elif length_pass < 8:
            print("Password 8 ta belgidan uzun bo`lishi kerak")
            student_password = input("Parolingizni kiriting: ")
            
        else:
            check_log_count = 0
            for user in range(len(student_date)):
                if student_date[user]['pas_log']['log'] == student_email:
                    print("Bunday gmail mavjud boshqacha nom bering")
                    student_email = input("Emailingizni kiriting: ")
                    check_log_count +=1
                    break
            if check_log_count:
                pass
            else:
                break
    student = {
            'name': student_name, 
            'course': [], 
            'pas_log': {'log': student_email, 
                        'pass': student_password
                        }}
    # pprint.pprint(student)
    return student

# paroli va logini bo`yicha bazada borligini aniqlovchi function
def login_student(students_data: list) -> str | None:
   
    # gmail va password ni kiriting 
    login = input("Emailingizni kiriting: ")
    passwod = input("Parolingizni kiriting: ")

    student_dict = {}
    student_dict['log'] = login
    student_dict['pass'] = passwod
    
    # bazada kiritilgan login va password ruyxatdan o`tgan yoki o`tmaganini tikshiramiz
    for user in students_data:
        if(user['pas_log']) == student_dict:
            print("Ro'yxatdan muvaffaqiyatli o'tildi, Xush kelibsiz {}.".format(user['name']))
            return user
    return None

# kursga yozilish uchun function
def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
 
    # kursni tanlash uchun nommir tanlash
    courses_number = int(input("Kurs raqamini kiriting: "))

    if courses_number - 1 > len(courses_data) or courses_number - 1 < 0:
        print("\nSiz tanlagan nommirda kurs yo`q iltimos tikshirib qaytadan tanlang!\n")
        return None
    else:
        print("Muvaffaqiyatli ro'yhatdan o'tildi {}!\n".format(courses_data[courses_number - 1]["course_name"]))
        return courses_data[courses_number - 1]
   