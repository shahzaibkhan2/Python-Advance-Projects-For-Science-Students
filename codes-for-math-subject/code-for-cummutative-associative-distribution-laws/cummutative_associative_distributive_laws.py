# Function for cummutative law
def commutative_law(a, b):
    # Addition: a + b = b + a
    addition_result = a + b
    addition_reversed = b + a
    addition_law = addition_result == addition_reversed

    # Multiplication: a * b = b * a
    multiplication_result = a * b
    multiplication_reversed = b * a
    multiplication_law = multiplication_result == multiplication_reversed

    return addition_law, multiplication_law


# Function for associative law
def associative_law(a, b, c):
    # Addition: (a + b) + c = a + (b + c)
    addition_result_1 = (a + b) + c
    addition_result_2 = a + (b + c)
    addition_law = addition_result_1 == addition_result_2

    # Multiplication: (a * b) * c = a * (b * c)
    multiplication_result_1 = (a * b) * c
    multiplication_result_2 = a * (b * c)
    multiplication_law = multiplication_result_1 == multiplication_result_2

    return addition_law, multiplication_law


# Function for distributive law
def distributive_law(a, b, c):
    # Left distributive law: a * (b + c) = (a * b) + (a * c)
    left_distributive_result_1 = a * (b + c)
    left_distributive_result_2 = (a * b) + (a * c)
    left_distributive_law = left_distributive_result_1 == left_distributive_result_2

    # Right distributive law: (a + b) * c = (a * c) + (b * c)
    right_distributive_result_1 = (a + b) * c
    right_distributive_result_2 = (a * c) + (b * c)
    right_distributive_law = right_distributive_result_1 == right_distributive_result_2

    return left_distributive_law, right_distributive_law


# Testing the laws with examples

# Commutative Law test
print("Commutative Law:")
print(commutative_law(3, 5))  # (Returns True,Returns True)
print(commutative_law(2, 4))  # (Returns True,Returns True)

# Associative Law test
print("\nAssociative Law:")
print(associative_law(2, 3, 4))  # (Returns True,Returns True)
print(associative_law(5, 7, 9))  # (Returns True,Returns True)

# Distributive Law test
print("\nDistributive Law:")
print(distributive_law(2, 3, 4))  # (Returns True,Returns True)
print(distributive_law(5, 6, 7))  # (Returns True,Returns True)
