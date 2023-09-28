class Student:
  def __init__(self,name,roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list, key=lambda Student: Student.cgpa,reverse = True)
  return sorted_students


Students = [
Student("hari", "A123","7.8"),
Student("Srikanth", "A124","8.9"),
Student("Saumya", "A125","9.1"),
Student("Mahidhar", "A126","9.9"),
]

sorted_students = sort_students(Students)

for Student in sorted_students:
  print("Name: {},Roll Number: {},CGPA: {}".format(Student.name,Student.roll_number,Student.cgpa))