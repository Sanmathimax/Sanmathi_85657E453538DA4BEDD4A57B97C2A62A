class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage
students = [
    Student("Diya", "A101", 4.8),
    Student("Enika", "B102", 3.5),
    Student("Naveen", "C103", 2.7),
    Student("Sanjeev", "D104", 5.9),
]

sorted_students = sort_students(students)

# Print the sorted students
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
