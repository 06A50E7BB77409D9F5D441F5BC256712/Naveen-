class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the student list based on CGPA in descending order
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Create a list of student objects
students = [
  Student("Alice", "A101", 9.8),
  Student("Bob", "A102", 7.9),
  Student("Charlie", "A103", 8.7),
  Student("David", "A104", 9.0),
]

# Sort the students by CGPA
sorted_students = sort_students(students)

# Print the sorted list
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
