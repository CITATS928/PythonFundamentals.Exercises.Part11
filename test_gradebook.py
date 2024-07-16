import unittest
from gradebook import AliveStatus,Person,Instructor,Student,ZipCodeStudent,CollegeStudent,Classroom

class TestGradebook(unittest.TestCase):

    def setUp(self):
        self.instructor = Instructor("John","Doe","date",1)
        self.student_zip = ZipCodeStudent("Jane","Smith","date",1)
        self.student_college=CollegeStudent("Alice","Johnson","date",1)
        self.classroom = Classroom()

    def test_add_instructor(self):
        self.classroom.add_Instructor(self.instructor)
        self.assertIn(self.instructor.instructor_id,self.classroom.instructors)

    def test_remove_instructor(self):
        self.classroom.add_Instructor(self.instructor)
        self.classroom.remove_Instructor(self.instructor.instructor_id)
        self.assertNotIn(self.instructor.instructor_id,self.classroom.instructors)

    
if __name__ == '__main__':
    unittest.main()