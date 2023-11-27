import random

def choose_multiplier():
    # Choose a multiplier value between 1.2 and 30
    multiplier = random.uniform(1.2, 30)

    # Apply a lower probability for numbers over 5
    if multiplier > 5:
        if random.random() < 0.2:  # Adjust the probability as needed
            multiplier *= random.uniform(1.2, 5)  # Choose a value between 1.2 and 5

    return multiplier

def choose_number():
    # Choose a number between 1 and 30
    number = random.uniform(1, 30)

    # Apply a lower probability for numbers over 15
    if number > 15:
        if random.random() < 0.3:  # Adjust the probability as needed
            number = random.uniform(1, 15)  # Choose a value between 1 and 15

    return number

# Example usage:
multiplier_value = choose_multiplier()
number_value = choose_number()

print("Chosen multiplier:", multiplier_value)
print("Chosen number:", number_value)
