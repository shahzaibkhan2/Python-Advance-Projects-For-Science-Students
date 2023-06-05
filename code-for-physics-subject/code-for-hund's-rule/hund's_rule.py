# Function to find number of electrons according to hund's rule
def hunds_rule(num_electrons):
    orbitals = []
    electrons_left = num_electrons

    while electrons_left > 0:
        max_electrons = min(2, electrons_left)
        orbitals.append(max_electrons)
        electrons_left -= max_electrons

    return orbitals
# Example for usage:
num_electrons = 10
orbital_config = hunds_rule(num_electrons)
print(f"Orbital configuration for {num_electrons} electrons: {orbital_config}")

