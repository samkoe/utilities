import random

# Define lists
students = ["student1", 
            "student2", 
            "student3", 
            "student3", 
            "student4", 
            "student5", 
            "student6"]
order = []

# Make random list of students
while len(order) != len(students):
    choice = random.choice(students)
    if choice not in order:
        order.append(choice)

# Print list to user
for i in range(1, len(order)):
    print(str(i) + ". " + order[i - 1])
