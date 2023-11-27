Course = ["MIT", "Cybersecurity", "Datascience"]

print(Course)

# Accessing an element in an array
print(Course[1])

# looping an array
for course in Course:
    print(course)

    # adding an element in an array
Course.append("Android Development")
print(Course)

# removing an element from an array
Course.remove("MIT")
print(Course)
