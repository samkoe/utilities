import random

# Define lists
students = ["krista", "liam", "riley", "kylee", "brandon", "matthew", "hannah", "garreth", "oscar", "maya", "isaac", "valerie"]
order = []

# Make random list of students
while len(order) != len(students):
    choice = random.choice(students)
    if choice not in order:
        order.append(choice)

# Print list to user
for i in range(1, len(order)):
    print(str(i) + ". " + order[i - 1])