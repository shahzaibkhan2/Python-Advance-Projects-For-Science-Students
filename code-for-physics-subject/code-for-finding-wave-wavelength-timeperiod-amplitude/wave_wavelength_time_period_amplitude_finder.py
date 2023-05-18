# Taking inputs
v = float(input("Enter the velocity of the wave in m/s: "))
f = float(input("Enter the frequency of the wave in Hz: "))

# Calculating wavelength
wavelength = v/f

# Calculating time period
time_period = 1/f

# Displaying wavelength and time period
print("The wavelength of the wave is {:.2f} m.".format(wavelength))
print("The time period of the wave is {:.2f} s.".format(time_period))

# Taking amplitude input
amplitude = float(input("Enter the amplitude of the wave in m: "))

# Displaying amplitude
print("The amplitude of the wave is {:.2f} m.".format(amplitude))
