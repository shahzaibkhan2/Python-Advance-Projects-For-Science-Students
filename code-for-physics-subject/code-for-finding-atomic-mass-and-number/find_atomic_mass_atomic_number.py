# Import periodictable module
from periodictable import elements

# Function to get atomic properties like symbols,atomic masses and numbers
def get_atomic_properties(element_symbol):
    try:
        element = elements.symbol(element_symbol)
        atomic_number = element.number
        atomic_mass = element.mass
        return atomic_number, atomic_mass
    except KeyError:
        return None, None

# Example for usage:
symbol = input("Enter the symbol of an element: ")
atomic_number, atomic_mass = get_atomic_properties(symbol)
if atomic_number and atomic_mass:
    print(f"Atomic number: {atomic_number}")
    print(f"Atomic mass: {atomic_mass} g/mol")
else:
    print("Invalid element symbol!")
