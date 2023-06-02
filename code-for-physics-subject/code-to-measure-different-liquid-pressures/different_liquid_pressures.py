# Import pressure module
import pressure

# Function to measure water pressure
def measure_water_pressure():
    water_pressure = pressure.water()
    print("Water Pressure: {:.2f} Pascal".format(water_pressure))

# Function to measure vapor pressure
def measure_vapor_pressure():
    vapor_pressure = pressure.vapor()
    print("Vapor Pressure: {:.2f} Pascal".format(vapor_pressure))

# Function to measure atmospheric pressure
def measure_atmospheric_pressure():
    atmospheric_pressure = pressure.atm()
    print("Atmospheric Pressure: {:.2f} Pascal".format(atmospheric_pressure))

# Function to measure liqiud pressure
def measure_liquid_pressure(density, depth):
    liquid_pressure = pressure.liquid(density, depth)
    print("Liquid Pressure: {:.2f} Pascal".format(liquid_pressure))

# Example for usage
measure_water_pressure()
measure_vapor_pressure()
measure_atmospheric_pressure()
measure_liquid_pressure(1000, 10)  # Assuming density of water as 1000 kg/m^3 and depth of 10 meters
