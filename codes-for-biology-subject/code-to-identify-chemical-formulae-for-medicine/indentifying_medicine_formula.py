# Function for parsing chemical formula
def parse_chemical_formula(formula):
    elements = {}
    current_element = ""
    current_count = ""
    for char in formula:
        if char.isalpha():
            if current_element != "":
                if current_count == "":
                    current_count = "1"
                elements[current_element] = elements.get(current_element, 0) + int(current_count)
                current_count = ""
            current_element = char
        elif char.isdigit():
            current_count += char
    if current_element != "":
        if current_count == "":
            current_count = "1"
        elements[current_element] = elements.get(current_element, 0) + int(current_count)
    return elements

# Function to execute main object
def main():
    formula = input("Enter the chemical formula: ")
    elements = parse_chemical_formula(formula)
    print("Chemical formula breakdown:")
    for element, count in elements.items():
        print(f"{element}: {count}")

# Main object
if __name__ == "__main__":
    main()
