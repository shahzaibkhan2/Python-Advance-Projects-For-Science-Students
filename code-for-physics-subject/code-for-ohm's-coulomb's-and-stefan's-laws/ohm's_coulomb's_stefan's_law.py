# Import math module
import math

# Function for Ohm's Law
def ohms_law(voltage, resistance):
    current = voltage / resistance
    return current

# Function for Coulomb's Law
def coulombs_law(charge1, charge2, distance):
    k = 9e9  # Coulomb's constant
    force = k * (charge1 * charge2) / (distance ** 2)
    return force

# Function for Stefan's Law
def stefans_law(temperature):
    sigma = 5.67e-8  # Stefan-Boltzmann constant
    energy_emitted = sigma * (temperature ** 4)
    return energy_emitted


# Ohm's Law test
print("Ohm's Law:")
voltage = 12  # volts
resistance = 4  # ohms
current = ohms_law(voltage, resistance)
print("Voltage:", voltage, "V")
print("Resistance:", resistance, "Ω")
print("Current:", current, "A")

# Coulomb's Law test
print("\nCoulomb's Law:")
charge1 = 2e-6  # coulombs
charge2 = 4e-6  # coulombs
distance = 1  # meter
force = coulombs_law(charge1, charge2, distance)
print("Charge 1:", charge1, "C")
print("Charge 2:", charge2, "C")
print("Distance:", distance, "m")
print("Force:", force, "N")

# Stefan's Law test
print("\nStefan's Law:")
temperature = 500  # Kelvin
energy_emitted = stefans_law(temperature)
print("Temperature:", temperature, "K")
print("Energy Emitted:", energy_emitted, "W/m^2")
