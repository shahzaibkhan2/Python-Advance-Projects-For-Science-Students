# Import intertools
from itertools import product


# Function to derive law of segregation
def law_of_segregation(parent_genotype):
    gametes = []
    for allele1 in parent_genotype[0]:
        for allele2 in parent_genotype[1]:
            gametes.append(allele1 + allele2)
    return gametes


# Function to derive law of independent assortment
def law_of_independent_assortment(parent_genotypes):
    offspring_genotypes = []
    for genotype1 in parent_genotypes[0]:
        for genotype2 in parent_genotypes[1]:
            offspring_genotypes.append(genotype1 + genotype2)
    return offspring_genotypes


# Law of Segregation test
parent_genotype = ["Aa", "Aa"]
gametes = law_of_segregation(parent_genotype)
print("Law of Segregation:")
print("Parent genotype:", parent_genotype)
print("Gametes:", gametes)

# Law of Independent Assortment test
parent_genotypes = [["Aa", "Aa"], ["Bb", "Bb"]]
offspring_genotypes = law_of_independent_assortment(parent_genotypes)
print("\nLaw of Independent Assortment:")
print("Parent genotypes:", parent_genotypes)
print("Offspring genotypes:", offspring_genotypes)
