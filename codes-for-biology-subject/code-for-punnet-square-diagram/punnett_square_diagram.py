# Function to generate punnett square
def generate_punnett_square(parent1, parent2):
    # Determine the alleles from parent 1
    p1_alleles = [parent1[i:i + 2] for i in range(0, len(parent1), 2)]

    # Determine the alleles from parent 2
    p2_alleles = [parent2[i:i + 2] for i in range(0, len(parent2), 2)]

    # Generate the Punnett square
    punnett_square = []
    for allele1 in p1_alleles:
        for allele2 in p2_alleles:
            punnett_square.append(allele1 + allele2)

    return punnett_square


# Function to display punnett square diagram
def display_punnett_square(punnett_square):
    # Display the Punnett square diagram
    header = " | ".join(punnett_square[0])
    separator = "-" * len(header)

    print(header)
    print(separator)

    for row in punnett_square[1:]:
        print(" | ".join(row))


# Example for usage
parent1 = "AaBb"
parent2 = "AaBb"

punnett_square = generate_punnett_square(parent1, parent2)
display_punnett_square(punnett_square)
