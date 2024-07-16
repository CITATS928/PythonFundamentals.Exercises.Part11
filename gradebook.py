from enum import Enum
import uuid
import unittest

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive
    
    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, alive):
        self.alive = alive

class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        super().__init__(first_name, last_name, dob, alive) ## Initialize the Person attributes
        self.instructor_id = f"Instructor_{uuid.uuid4()}"   ## Unique instructor ID with a UUID


class Student(Person):
    def __init__(self, first_name, last_name, dob, alive=AliveStatus.Alive):
        super().__init__(first_name, last_name, dob, alive) # Initialize the Person attributes
        self.student_id = f"Student_{uuid.uuid4()}"     # Unique student ID with a UUID

class ZipCodeStudent(Student):
    pass

class CollegeStudent(Student):
    pass

class Classroom:
    def __init__(self):
        self.students = {}      # Dictionary to store students by their student_id
        self.instructors = {}   # Dictionary to store instructors by their instructor_id

    def add_Instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor

    def remove_Instructor(self, instructor_id):
        if instructor_id in self.instructors:
            del self.instructors[instructor_id]

    def add_Student(self, student):
        self.students[student.student_id] = student

    def remove_Student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def print_Instructors(self):
        for instructor_id, instructor in self.instructors.items():
            print(f"{instructor_id}: {instructor.first_name} {instructor.last_name}")

    def print_Students(self):
        for student_id, student in self.students.items():
            print(f"{student_id}: {student.first_name} {student.last_name}")

if __name__ == "__main__":
    pass

class TestGradebook(unittest.TestCase):

    def setUp(self):
        self.instructor = Instructor("John", "Doe", "date")
        self.student_zip = ZipCodeStudent("Jane", "Smith", "date")
        self.student_college = CollegeStudent("Alice", "Johnson", "date")
        self.classroom = Classroom()

    def test_add_instructor(self):
        self.classroom.add_Instructor(self.instructor)
        self.assertIn(self.instructor.instructor_id, self.classroom.instructors)

    def test_remove_instructor(self):
        self.classroom.add_Instructor(self.instructor)
        self.classroom.remove_Instructor(self.instructor.instructor_id)
        self.assertNotIn(self.instructor.instructor_id, self.classroom.instructors)

if __name__ == '__main__':
    unittest.main()
