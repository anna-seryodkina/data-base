import psycopg2


def faculty_exists(number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from faculties where number = (%s)", (number,))

    rows = cur.fetchall()

    if(len(rows) != 0):
        return True;
    else:
        return False;

    cur.close()
    con.close()


def student_exists(student_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from students where id = (%s)", (student_id,))

    rows = cur.fetchall()

    if(len(rows) != 0):
        return True;
    else:
        return False;

    cur.close()
    con.close()


def subject_exists(name, lecture_hall_number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from subjects where name = (%s) and lecture_hall_number = (%s)", (name, str(lecture_hall_number)))

    rows = cur.fetchall()

    if(len(rows) != 0):
        return True;
    else:
        return False;

    cur.close()
    con.close()


def teacher_exists(teacher_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from teachers where id = (%s)", (str(teacher_id),))

    rows = cur.fetchall()

    if(len(rows) != 0):
        return True;
    else:
        return False;

    cur.close()
    con.close()


def student_faculty_exists(st_id, fac_num):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from students_faculties where student_id = (%s) and faculty_number = (%s)", (str(st_id), str(fac_num)))

    rows = cur.fetchall()

    if(len(rows) != 0):
        return True;
    else:
        return False;

    cur.close()
    con.close()




def print_all_fac():
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("select * from faculties")

    rows = cur.fetchall()

    for r in rows:
        print(f"{r[0]} | {r[1]}")


    cur.close()
    con.close()


def print_all_students():
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()

    for r in rows:
        print(f"{r[1]} | {r[0]} {r[2]}")


    cur.close()
    con.close()


def print_all_subj():
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("select * from subjects")

    rows = cur.fetchall()

    for r in rows:
        print(f"{r[0]} | hall: {r[1]} at {r[2]}")


    cur.close()
    con.close()


def print_all_teachers():
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("select * from teachers")

    rows = cur.fetchall()

    for r in rows:
        print(f"{r[0]} | {r[1]} [{r[2]}]")


    cur.close()
    con.close()




def add_faculty(name, number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("insert into faculties (name, number) values (%s, %s)", (name, number) )

    con.commit()

    cur.close()
    con.close()


def add_student_faculty(st_id, fac_num):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("insert into students_faculties (student_id, faculty_number) values (%s, %s)", (st_id, fac_num) )

    con.commit()

    cur.close()
    con.close()


def add_student(st_id, first_name, last_name):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("insert into students (id, first_name, last_name) values (%s, %s, %s)", (st_id, first_name, last_name) )

    con.commit()

    cur.close()
    con.close()


def add_subject(name, lecture_hall_number, time, faculty_number, teacher_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("insert into subjects (name, lecture_hall_number, time, faculty_number, teacher_id) values (%s, %s, %s, %s, %s)",
                (name, lecture_hall_number, time, faculty_number, teacher_id) )

    con.commit()

    cur.close()
    con.close()


def add_teacher(id, name, department):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("insert into teachers (id, name, department) values (%s, %s, %s)", (id, name, department) )

    con.commit()

    cur.close()
    con.close()




def delete_faculty(number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("delete from faculties where number = (%s)", (number,))
 
    con.commit()

    cur.close()
    con.close()


def delete_student(student_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("delete from students where id = (%s)", (student_id,))
 
    con.commit()

    cur.close()
    con.close()


def delete_subject(name, lecture_hall_number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("delete from subjects  where name = (%s) and lecture_hall_number = (%s)", (name, str(lecture_hall_number)) )
 
    con.commit()

    cur.close()
    con.close()


def delete_teacher(teacher_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute("delete from teachers where id = (%s)", (str(teacher_id),))
 
    con.commit()

    cur.close()
    con.close()




def update_faculty(name, number):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor("update faculties set name = (%s) where number = (%s)", (name, number))
    cur.execute()
 
    con.commit()

    cur.close()
    con.close()


def update_student(st_id, first_name, last_name):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor("update students set first_name = (%s), last_name = (%s) where student_id = (%s)", (first_name, last_name, st_id))
    cur.execute()
 
    con.commit()

    cur.close()
    con.close()


def update_subject(name, lecture_hall_number, time, faculty_number, teacher_id):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor(
        "update subjects set time = (%s), faculty_number = (%s), teacher_id = (%s) where name = (%s) and lecture_hall_number = (%s)",
        (time, faculty_number, teacher_id, name, lecture_hall_number))
    cur.execute()
 
    con.commit()

    cur.close()
    con.close()


def update_teacher(id, name, department):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor("update teachers set name = (%s), department = (%s) where id = (%s)", (name, department, id))
    cur.execute()
 
    con.commit()

    cur.close()
    con.close()




def generate_faculty(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute(
        "INSERT into faculties (name, number)\
        SELECT chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),\
                trunc(random()*1000 - 1)::int\
        FROM generate_series(1, (%s)) s(i);", (str(n),) )
 
    con.commit()

    cur.close()
    con.close()


def generate_student(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute(
        "INSERT into students (id, first_name, last_name)\
        SELECT trunc(random()*1000)::int,\
                chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),\
                substr(md5(random()::text), 1, 8)\
        FROM generate_series(1, (%s)) s(i);", (str(n),) )
 
    con.commit()

    cur.close()
    con.close()


def generate_subject(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute(
        "INSERT into subjects (name, lecture_hall_number, time, faculty_number, teacher_id)\
        SELECT substr(md5(random()::text), 1, 8),\
                trunc(random()*1000)::int,\
                substr(md5(random()::text), 1, 8),\
                trunc(random()*1000)::int,\
                trunc(random()*1000)::int\
        FROM generate_series(1, (%s)) s(i);", (str(n),) )
 
    con.commit()

    cur.close()
    con.close()


def generate_teacher(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()
    cur.execute(
        "INSERT into teachers (id, name, department)\
        SELECT trunc(random()*1000)::int,\
                chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int) || chr(trunc(65+random()*25)::int),\
                substr(md5(random()::text), 1, 8)\
        FROM generate_series(1, (%s)) s(i);", (str(n),) )
 
    con.commit()

    cur.close()
    con.close()




def search1(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from subjects cross join teachers where subjects.teacher_id = teachers.id and department > (%s)", (str(n),))

    con.commit()

    cur.close()
    con.close()


def search2(n):
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select * from subjects cross join faculties where subjects.faculty_number = faculties.number and lecture_hall_number =  (%s)", (str(n),))
 
    con.commit()

    cur.close()
    con.close()


def search3():
    con = psycopg2.connect(host = "localhost", database = "myDB",
                user = "postgres", password = "postgresServer")

    cur = con.cursor()

    cur.execute("select subjects.name, lecture_hall_number, time, teachers.name, department from subjects cross join teachers where subjects.teacher_id = teachers.id")
 
    con.commit()

    cur.close()
    con.close()