# Import math module
import math

# Function for calculating logarithm
def calculate_logarithm(base, num):
    return math.log(num, base)

# Function to find exponential
def calculate_exponential(base, num):
    return math.pow(base, num)

# Example for usage
base = 12
num = 110

logarithm_result = calculate_logarithm(base, num)
exponential_result = calculate_exponential(base, num)

print(f"The logarithm of {num} to the base {base} is: {logarithm_result}")
print(f"The exponential of {num} to the base {base} is: {exponential_result}")
