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

################################################################################
#DEFINE FUNCTIONS
################################################################################

#Get key by value
def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

#Find amino acid sequence from a codon sequence
def amino_acid_sequence(codon_sequence):
    amino_acid_sequence=[]
    for i in codon_sequence:
        a=get_amino_acid(i)
        amino_acid_sequence.append(a)
    return amino_acid_sequence

#Return CG optimised codon
def CG_optimised_codon(amino_acid):
    amino=str(amino_acid)
    codon_amino_acid_map={}
    best_codons=[]
    with open("codon-aminoacid.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            codon_row = row["codon"]
            amino_acid = row["aminoacid"]
            codon_amino_acid_map[codon_row] = amino_acid
        matches=getKeysByValue(codon_amino_acid_map,amino)
        temp_count_dict={}
        for i in matches:
            count=i.count('C')+i.count('G')
            if i not in temp_count_dict:                                    #if avoids double ups
                temp_count_dict[i]=count
                #select codon with highest character count
                all_values = temp_count_dict.values()                       #converts values to string
                max_value = max(all_values)
                best_codons=getKeysByValue(temp_count_dict,max_value)
    return best_codons

#Find the comparable codon sequence with the most number of C and G bases
def find_CG_optimised_codon_sequence(amino_acid_sequence):
    CG_optimised_virus=[]
    for i in amino_acid_sequence:
        codon_options=CG_optimised_codon(i)
        if i in codon_options:
            CG_optimised_virus.append(i)
        else:
            CG_optimised_virus.append(codon_options[0])
    return CG_optimised_virus

#Compare two lists
def compare_2_lists(sequence_1,sequence_2):
    if sequence_1==sequence_2:
        print("The lists match")
    else:
        print("The lists are different")

################################################################################
#DEFINE KEY DATA STRUCTURES
################################################################################

#Define codon sequence for virus and vacine
vacine_codons=read_codons("vacine.txt")
virus_codons=read_codons("virus.txt")

#Find the amino acid sequence of the virus
virus_amino_sequence=[]
for i in virus_codons:
    virus_amino=get_amino_acid(i)
    virus_amino_sequence.append(virus_amino)



################################################################################
#DEFINE AND TEST ENGINEERED CODONS
################################################################################

#engineered codon sequence
engineered_virus_codons=find_CG_optimised_codon_sequence(virus_amino_sequence)

#engineered amino sequence
engineered_virus_aminos=amino_acid_sequence(engineered_virus_codons)


################################################################################
#UNDER DEVELOPMENT :: STEPWISE CG CODON REMOVAL
################################################################################
