import model

class EntityException(Exception):
    def __init__(self, message):
        self.message = message

class InputException(Exception):
    def __init__(self, message):
        self.message = message



def select_entity():
    print("entities:")
    print("> faculty\n> student\n> subject\n> teacher")
    entity = input("enter entity: ")
    if entity != "faculty" and entity != "student" and entity != "subject" and entity != "teacher":
        raise EntityException('>> oops. this entity does not exist.')
    else:
        return entity


def add():
    entity = select_entity()

    if entity == "faculty":
        try:
            name_inp = input("name: ")
            name = name_inp
            num_inp = input("number: ")
            number = int(num_inp)
        except:
            raise InputException(">> incorrect input.")

        if model.faculty_exists(number):
            raise EntityException(">> sorry, faculty with this number already exists.")
        else:
            model.add_faculty(name, number)

    elif entity == "student":
        try:
            st_id = int(input("student id: "))
            first_name = input("first name: ")
            last_name = input("last name: ")
        except:
            raise InputException(">> incorrect input.")

        if model.student_exists(student_id):
            raise EntityException(">> sorry, student with this id already exists.")
        else:
            model.add_student(st_id, first_name, last_name)

    elif entity == "subject":
        try:
            name = input("name: ")
            lecture_hall_number = int(input("lecture hall number: "))
            time = input("time: ")
            fac_num = int(input("faculty number: "))
            teacher_id = int(input("teacher id: "))
        except:
            raise InputException(">> incorrect input.")

        if model.subject_exists(name, lecture_hall_number):
            raise EntityException(">> sorry, this subject already exists.")
        else:
            if not model.faculty_exists(fac_num):
                raise EntityException(">> sorry, this faculty does not exist.")
            else:
                if not model.teacher_exists(teacher_id):
                    raise EntityException(">> sorry, this teacher does not exist.")
                else:
                    model.add_subject(name, lecture_hall_number, time, fac_num, teacher_id)

    elif entity == "teacher":
        try:
            t_id = int(input("id: "))
            name = input("name: ")
            dep = input("department: ")
        except:
            raise InputException(">> incorrect input.")

        if model.teacher_exists(t_id):
            raise EntityException(">> sorry, teacher with this id already exists.")
        else:
            model.add_teacher()



def delete():
    entity = select_entity()

    if entity == "faculty":
        try:
            num_inp = input("number: ")
            number = int(num_inp)
        except:
            raise InputException(">> incorrect input.")

        if model.faculty_exists(number):
            model.delete_faculty(number)
        else:
            raise EntityException(">> sorry, faculty does not exist.")

    elif entity == "student":
        try:
            st_id = int(input("student id: "))
        except:
            raise InputException(">> incorrect input.")

        if model.student_exists(st_id):
            model.delete_student(st_id)
        else: 
            raise EntityException(">> sorry, student does not exist.")

    elif entity == "subject":
        try:
            name = input("name: ")
            lecture_hall_number = int(input("lecture hall number: "))
        except:
            raise InputException(">> incorrect input.")

        if model.subject_exists(name, lecture_hall_number):
            model.delete_subject()
        else:
            raise EntityException(">> sorry, subject does not exist.")

    elif entity == "teacher":
        try:
            t_id = int(input("teacher id: "))
        except:
            raise InputException(">> incorrect input.")

        if model.teacher_exists(t_id):
            model.delete_teacher()
        else:
            raise EntityException(">> sorry, teacher does not exist.")



def update():
    entity = select_entity()

    if entity == "faculty":
        try:
            num_inp = input("what faculty you want to update? number: ")
            number = int(num_inp)
            if not model.faculty_exists(number):
                raise EntityException(">> sorry, this faculty does not exist.")
        except:
            raise InputException(">> incorrect input.")

        try:
            name_inp = input("enter new info. name: ")
            name = name_inp
        except:
            raise InputException(">> incorrect input.")

        model.update_faculty(name, number)

    elif entity == "student":
        try:
            student_id = int(input("what student you want to update? student_id: "))
            if not model.student_exists(student_id):
                raise EntityException(">> sorry, this student does not exist.")
        except:
            raise InputException(">> incorrect input.")

        try:
            print("enter new info.")
            first_name = input("first name: ")
            last_name = input("last name: ")
        except:
            raise InputException(">> incorrect input.")

        model.update_student(st_id, first_name, last_name)

    elif entity == "subject":
        try:
            name = input("what subject you want to update? name: ")
            lecture_hall_number = int(input("lecture_hall_number: "))
            if not model.subject_exists(name, lecture_hall_number):
                raise EntityException(">> sorry, this subject does not exist.")
        except:
            raise InputException(">> incorrect input.")

        try:
            print("enter new info...")
            time = input("time: ")
            fac_num = int(input("faculty number: "))
            teacher_id = int(input("teacher id: "))
        except:
            raise InputException(">> incorrect input.")

        if not model.faculty_exists(fac_num):
                raise EntityException(">> sorry, this faculty does not exist.")
        else:
            if not model.teacher_exists(teacher_id):
                raise EntityException(">> sorry, this teacher does not exist.")
            model.update_subject(name, lecture_hall_number, time, fac_num, teacher_id)

    elif entity == "teacher":
        try:
            teacher_id = int(input("what student you want to update? teacher_id: "))
            if not model.teacher_exists(teacher_id):
                raise EntityException(">> sorry, this teacher does not exist.")
        except:
            raise InputException(">> incorrect input.")

        try:
            print("enter new info.")
            name = input("name: ")
            dep = input("department: ")
        except:
            raise InputException(">> incorrect input.")

        model.update_teacher(teacher_id, name, dep)


def get_amount():
    try:
        amount = int(input("how many: "))
    except:
        raise InputException(">> incorrect input.")

    return amount


def generate():
    entity = select_entity()
    amount = get_amount()

    if entity == "faculty":
        model.generate_faculty(amount)

    elif entity == "student":
        model.generate_student(amount)

    elif entity == "subject":
        model.generate_subject(amount)

    elif entity == "teacher":
        model.generate_teacher(amount)



def search():
    n = input("what search? [1/2/3]")

    if n == "1":
        try:
            n = int(input("enter number. department bigger than: "))
        except:
            raise InputException(">> incorrect input.")

        model.search1(n)

    elif n == "2":
        try:
            n = int(input("enter lecture hall number: "))
        except:
            raise InputException(">> incorrect input.")

        model.search2(n)

    elif n == "3":
        model.search3()
    else:
        raise InputException(">> incorrect input.")