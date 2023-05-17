# Function which converts joule to calorie
def joule_to_calorie(joules):
    calories = joules * 0.239006
    return calories

# Function which converts calorie to joule
def calorie_to_joule(calories):
    joules = calories * 4.184
    return joules

# Function which converts joule to electron volt
def joule_to_electron_volt(joules):
    electron_volts = joules * 6.242e+18
    return electron_volts

# Function which converts electron vold to joule
def electron_volt_to_joule(electron_volts):
    joules = electron_volts / 6.242e+18
    return joules

# Function for main
def main():
    print("Energy Conversion Code")
    print("-------------------------")
    print("1. Joule to Calorie")
    print("2. Calorie to Joule")
    print("3. Joule to Electron Volt")
    print("4. Electron Volt to Joule")
    print("-------------------------")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        joules = float(input("Enter the energy in Joules: "))
        calories = joule_to_calorie(joules)
        print(f"The energy in calories is: {calories}")
    elif choice == 2:
        calories = float(input("Enter the energy in calories: "))
        joules = calorie_to_joule(calories)
        print(f"The energy in Joules is: {joules}")
    elif choice == 3:
        joules = float(input("Enter the energy in Joules: "))
        electron_volts = joule_to_electron_volt(joules)
        print(f"The energy in electron volts is: {electron_volts}")
    elif choice == 4:
        electron_volts = float(input("Enter the energy in electron volts: "))
        joules = electron_volt_to_joule(electron_volts)
        print(f"The energy in Joules is: {joules}")
    else:
        print("Invalid choice. Please try again.")

# If __name__=="__main__" for safe execution of main function to avoid unnecessary executions
if __name__ == "__main__":
    main()
