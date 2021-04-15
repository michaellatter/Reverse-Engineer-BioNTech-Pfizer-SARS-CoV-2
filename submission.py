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
    return codon_amino_acid_map[codon]   #matches codon to amino acid

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
    return codons   #reads in codons three at a time, omits any white spaces   #takes csv file and outputs list

def compare(attempt, target):

    count = 0
    for i in range(len(target)):
        if attempt[i] == target[i]:
            count += 1
    return 100 * count / len(target)

vacine_codons=read_codons("vacine.txt")
virus_codons=read_codons("virus.txt")

#what codons match
matching_codons = ()
best_codons = ()

for i in virus_aminos:
    matching_codons.append=get_codons(i)            ###identify all matching codons
    if C or G in matching_codons:                   #do any of the strings in matching codons have a C or a G
        a=select_highest_codon(matching_codons)     ###y, select highest codon
        best_codon.append(a)                        #
        optimised.append(a)
    else:
        index=index number i
        wild_type_codon = virus_codons[1]
        optimised.append()=wild_type_codon

#get codons = finds all matching codons and prints as list
#select highest codon = looks at a list of strings and selects the string with the most C and G


CG_count=
    if C or G in alternative_codon[i]:
        CG_count+=1

alt=["ACC"]
pres=["ATA"]

map={ACC: M , ATA : M}


* create virus amino acid list
* move though amino list
    *for i, what codons match
        *add codon to temp_dict
        *count
2. if codon matches this amino, add to temp list
3. for each item in the list, count how many c and g it has , map this number to codon in temp list
4. select the codon highst maped number in temp list
5. is this codon the codon in the virus, true, false
6. if false, replace i with this codon

*C G count for each codon, mapped to codon
* order codon map from most amount of C to least
*move through codon map until amino matches
    *add this codon to new strand


create dict with codons + c and g count

--------------------------------------------------------------------------------
#REPLACE PRESENT CODON WITH ALTERNATIVE
if c or g in alternative_codon:
    replace i with alternative

--------------------------------------------------------------------------------
#REDUCE NUMBER OF ALTERNATIVE CODONS TO OPTIMISE DENATURATION
