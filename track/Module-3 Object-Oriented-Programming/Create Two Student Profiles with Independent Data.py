class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance variables
        self.student_id = student_id
        self.name = name
        self.course = course

first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

# Create the first StudentProfile object
student_first = StudentProfile(first_id, first_name, first_course)

# Create the second StudentProfile object
student_second = StudentProfile(second_id, second_name, second_course)

# Print the first student's data
print("Student 1")
print(f"ID: {first_id}")
print(f"Name: {first_name}")
print(f"Course: {first_course}")

# Print the second student's data
print("Student 2")
print(f"ID: {second_id}")
print(f"Name: {second_name}")
print(f"Course: {second_course}")