import psycopg2

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, REAL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists
from sqlalchemy import ForeignKey, Table



Base = declarative_base()



students_faculties_association = Table ('students_faculties', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('faculty_number', Integer, ForeignKey('faculties.number'))
)



class Student(Base):
    __tablename__ = "students"
    first_name = Column(String)
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    faculties = relationship("Faculty", secondary=students_faculties_association)


class Faculty(Base):
    __tablename__ = "faculties"
    name = Column(String)
    number = Column(Integer, primary_key=True)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String())
    department = Column(String)


class Subject(Base):
    __tablename__ = "subjects"
    name = Column(String(), primary_key=True)
    lecture_hall_number = Column(String(), primary_key=True)
    time = Column(String)
    faculty_number = Column(Integer, ForeignKey(Faculty.number))
    teacher_id = Column(Integer, ForeignKey(Teacher.id))



DATABASE_URI = 'postgres+psycopg2://postgres:postgresServer@localhost:5432/myDB'

engine = create_engine(DATABASE_URI)

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def faculty_exists(f_number):
    s = Session()
    res = s.query(exists().where(Faculty.number == f_number)).scalar()
    s.close()

    return res


def student_exists(st_id):
    s = Session()
    res = s.query(exists().where(Student.id == st_id)).scalar()
    s.close()
    return res


def subject_exists(name, lecture_hall_number):
    s = Session()
    res = s.query(exists().where(and_(
            Subject.name == name,
            Subject.lecture_hall_number == lecture_hall_number ))).scalar()
    s.close()
    return res


def teacher_exists(t_id):
    s = Session()
    res = s.query(exists().where(Teacher.id == t_id)).scalar()
    s.close()
    return res




def add_faculty(f_name, f_number):
    s = Session()

    faculty = Faculty(
        name = f_name,
        number = f_number
    )

    s.add(faculty)
    s.commit()

    s.close()


def add_student(st_id, first_name, last_name):
    s = Session()

    student = Student(
        first_name = first_name,
        id = st_id,
        last_name = last_name
    )
    
    s.add(student)
    s.commit()

    s.close()


def add_subject(s_name, s_lecture_hall_number, s_time, s_faculty_number, s_teacher_id):
    s = Session()

    subj = Subject(
        name = s_name,
        lecture_hall_number = s_lecture_hall_number,
        time = s_time,
        faculty_number = s_faculty_number,
        teacher_id = s_teacher_id
    )
    
    s.add(subj)
    s.commit()

    s.close()


def add_teacher(t_id, t_name, t_department):
    s = Session()

    t = Teacher(
        id = t_id,
        name = t_name,
        department = t_department
    )
    
    s.add(t)
    s.commit()

    s.close()




def delete_faculty(number):
    s = Session()

    f = s.query(Faculty).filter(Faculty.number==number).first()

    s.delete(f)
    s.commit()

    s.close()


def delete_student(student_id):
    s = Session()

    st = s.query(Student).filter(Student.id==student_id).first()

    s.delete(st)
    s.commit()

    s.close()


def delete_subject(name, lecture_hall_number):
    s = Session()

    subj = s.query(Subject).filter(
        and_(
            Subject.name == name,
            Subject.lecture_hall_number == lecture_hall_number
        )
    ).first()

    s.delete(subj)
    s.commit()

    s.close()


def delete_teacher(teacher_id):
    s = Session()

    t = s.query(Teacher).filter(Teacher.id==teacher_id).first()

    s.delete(t)
    s.commit()

    s.close()




def update_faculty(name, number):
    s = Session()

    faculty = Faculty(
        name = f_name,
        number = f_number
    )

    s.update(faculty)
    s.commit()

    s.close()


def update_student(st_id, first_name, last_name):
    s = Session()

    student = Student(
        first_name = first_name,
        id = st_id,
        last_name = last_name
    )
    
    s.update(student)
    s.commit()

    s.close()


def update_subject(name, lecture_hall_number, time, faculty_number, teacher_id):
    s = Session()

    subj = Subject(
        name = s_name,
        lecture_hall_number = s_lecture_hall_number,
        time = s_time,
        faculty_number = s_faculty_number,
        teacher_id = s_teacher_id
    )
    
    s.update(subj)
    s.commit()

    s.close()


def update_teacher(id, name, department):
    s = Session()

    t = Teacher(
        id = t_id,
        name = t_name,
        department = t_department
    )
    
    s.update(t)
    s.commit()

    s.close()

