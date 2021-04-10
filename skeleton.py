# Program to optimise codons of a virus in an attempt to create a vaccine
import csv  #  Allow reading of CSV files


# Used to store a dictionary mapping codons to the amino acids they encode
codon_amino_acid_map = {}


def get_amino_acid(codon):
    """
      Returns a character representing the amino acid encoded by the given codon.
      Note: Includes bugfix from Lucas Martins
    """
    if len(codon_amino_acid_map) <= 0:
        with open("codon-aminoacid.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                codon_row = row["codon"]
                amino_acid = row["aminoacid"]
                codon_amino_acid_map[codon_row] = amino_acid
    return codon_amino_acid_map[codon]


def read_codons(filename):
    """
      Reads in codons from the given file, placing them in order in the returned list.
    """
    codons = []
    with open(filename) as input_file:
        #  Read in three characters at a time, since each codon is three characters
        data = input_file.read(3)
        while data.strip() != "":
            codons.append(data)
            data = input_file.read(3)
    return codons


def compare(attempt, target):
    """
    Compares the given attempt to determine the percentage of
    codons in the given attempt match those in the target

    Arguments:
    attempt -- A list of codons to be compared with the target
    target -- A list of codons to be compared to

    Returns the percentage of codons that are identical between the attempt and the target
    """
    count = 0
    for i in range(len(target)):
        if attempt[i] == target[i]:
            count += 1
    return 100 * count / len(target)


def optimise_codons(codons):
    """
      Optimises the given codons using the method specified in readme.md.

      Arguments:
      codons -- A list of codons to optimise

      Returns an optimised list of codons
    """
    optimised = []
    for codon in codons:
        #  TODO: Do something better than just copying the input
        optimised.append(codon)
    return optimised


if __name__ == "__main__":
    #  Read in virus
    virus = read_codons("virus.txt")
    #  Read in vaccine
    vaccine = read_codons("vaccine.txt")

    #  Optimise
    optimised = optimise_codons(virus)

    #  Compare virus and optimised version to vaccine
    virus_comparison = compare(virus, vaccine)
    optimised_comparison = compare(optimised, vaccine)

    #  Output results, including improvement from optimisation
    print("Virus comparison: {:.2f}% identical to vaccine".format(virus_comparison))
    print("Optimised comparison: {:.2f}% identical to vaccine".format(optimised_comparison))
    print("Optimisation improves compatability by {:.2f}%".format(optimised_comparison - virus_comparison))


