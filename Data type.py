# Data type
number = 25  # int
second = 56.78  # float
text = "Hello there"  # str
ispythonintresting = True  # bool

# store multiple values in a single variable
cars = ["toyota", "nissan", "vw"]  # list #ordered and changeable
fruits = ("banana", "orange", "apple")  # tuple #unordered and unchangeable
countries = {"Kenya", "Tunisia", "Algeria"}  # set # unordered and unchangeable
details = {
    "firstname": "Andrew",
    "age": 34,
    "course": "web development",
    "nationality": "kenyan"
}  # dictionary - key value pair

print(details["course"])
print(second)
print(text)
print(ispythonintresting)
print(cars)
print(countries)
print(details)

# determine a data type
print(type(number))
print(type(details))
print(type(countries))

# Typecasting - converting one data type to another
print(float(number))
print(int(second))
