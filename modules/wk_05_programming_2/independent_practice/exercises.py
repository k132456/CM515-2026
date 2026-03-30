### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will evaluate your submissions myself with this exact script.

# This dictionary of RNA codons to amino acid symbols may be useful for some exercises!
codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

# You will likely need this package for list_files()
import os


### PART 1: ANALYZING SEQUENCES ###

# This function determines whether two string sequences are equivalent: returns True if they are equivalent, and False if they are not.
def check_equivalence(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    #print(seq_1 == seq_2)
    if seq_1 == seq_2:
        x = True
    elif seq_1 != seq_2:
        x = False
    #print(x)
    return x

    ### YOUR CODE ABOVE HERE ###

# This function takes two string sequences and returns a list of the positions where they differ. Returns an empty list if the sequences are identical.
# You may assume both sequences are the same length.
def get_variants(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###

    variant_list = []
    seq_1_list = list(seq_1) # use list() method to separate a string so that every single character is a separate element
    seq_2_list = list(seq_2)
    #print(seq_1_list)
    #print(seq_2_list)
    if seq_1 != seq_2:
        for x in range(len(seq_1_list)):
            if seq_1_list[x] != seq_2_list[x]:
                #diff_spot = seq_1_list.index(seq_1_list[x]) #this doesn't work
                #print(diff_spot)
                #variant_list.append(diff_spot) #doesn't work see line 49
                variant_list.append(x)
                #print(variant_list)
    elif seq_1 == seq_2:
        variant_list.clear()
    

        
    
    ### YOUR CODE ABOVE HERE ###

    return variant_list
    #print(variant_list)

# This function takes a string sequence and returns the type of sequence it is: DNA, RNA, protein, or unknown.
# Note: Technically, there are some sequences that could match multiple types. You can ignore these edge cases for this exercise.
def get_seq_type(seq):

    # You may use these lists if you want to!
    dna_chars = ["A", "G", "C", "T"]
    rna_chars = ["A", "G", "C", "U"]
    aa_chars = codon_dict.values()#.unique()

    ### YOUR CODE BELOW HERE ###
    #asking: do all items in seq exist in set(dna_chars)
    seq_set = set(seq)
    
    dna_set = set(dna_chars)
    x = seq_set.issubset(dna_set)


    rna_set = set(rna_chars)
    y = seq_set.issubset(rna_set)


    aa_set = set(aa_chars)
    z = seq_set.issubset(aa_set)

    if x:
        seq_type = "DNA"
        #print("This is DNA")
    elif y:
        seq_type = "RNA"
        #print("This is DNA")
    elif z:
        seq_type = "protein"
    elif not y or not x:
        seq_type = "unknown"
        #print("This is unknown")

    #print(seq_type)
    return seq_type

# This function has been written for you. You may use it in type_of_point_mutation() if you want to!
def split_rna_to_codons(rna_seq):
    codon_list = []
    for i in range(0, len(rna_seq), 3):
        codon_list.append(rna_seq[i:i+3])
    return codon_list

# This function takes two RNA string sequences and returns the type of point mutation that differentiates them: silent, missense, or nonsense. 
# Return "none" if the sequences are identical. You can assume there is at most one point mutation between the two sequences, and that the sequences are of equal length.
# Hint: You can use the functions you already wrote above, and/or get_protein_seq() from last week's assignment 2.
def type_of_point_mutation(seq_1, seq_2):

    ### YOUR CODE BELOW HERE ###


    seq_1_codon_list = split_rna_to_codons(seq_1)
    seq_2_codon_list = split_rna_to_codons(seq_2)




    if seq_1 != seq_2:
        for codons in range(len(seq_1_codon_list)):
            if seq_1_codon_list[codons] != seq_2_codon_list[codons]:
                x = codon_dict.get(seq_1_codon_list[codons])
                y = codon_dict.get(seq_2_codon_list[codons])
                if x == y:
                    mutation_type = "silent"
                elif x != y and x != "*" and y != "*":
                    mutation_type = "missense"
                elif x == "*" or y == "*":
                    mutation_type = "nonsense"
    
    elif seq_1 == seq_2:
        mutation_type = "none"

    #print(mutation_type)
    
    ### YOUR CODE ABOVE HERE ###

    
    return mutation_type


### PART 2: FILES ###

# This function returns the list of files in the current directory.
def list_files():

    ### YOUR CODE BELOW HERE ###

    files_list = []
    for items in os.scandir():
        if items.is_file():
            files_list.append(items.name)
    
    #print(files_list)

    ### YOUR CODE ABOVE HERE ###

    return files_list

# This function returns a list of all the header lines (start with '>') in a given FASTA file.
def extract_fasta_headers(filepath):

    ### YOUR CODE BELOW HERE ###

    header_list = []
    with open (filepath, "r") as fasta_file:
        #lines_list = fasta_file.readline()
        for line in fasta_file:
            if line.startswith(">"):
                header_list.append(line.strip("\n"))
    #print(header_list)


    ### YOUR CODE ABOVE HERE ###
    #print(header_list)

    return header_list


### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###

#this_seq = "Woah!"
#that_seq = "Weee!"
#check_equivalence(this_seq, that_seq)



#alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#def callalph(alpha):
#    print(alpha[2])

#callalph(alphabet1)

#this_string_seq = "AAABAAAABAAAAAB"
#that_string_seq = "AAAAAAAAAAAAAAA"
#this_string_seq = "AAAAAAAAAAAAAAA"
#get_variants(this_string_seq, that_string_seq)

#dna_string = "ATCGCTCGAGCTCGA"
#get_seq_type(dna_string)

#rna_string = "ACGUGCUGAUGUGCUGAUUCG"
#get_seq_type(rna_string)

#aa_string = "DVNIHLY"
#get_seq_type(aa_string)

#unknown_string = "9948767868"
#get_seq_type(unknown_string)

#confuse_string1 = "AGTCGCTGATCG8"
#get_seq_type(confuse_string1)

#my_rna_seq = "AUUGAGAGACGUCCA"
#split_rna_to_codons(my_rna_seq)
#print(codon_list)


#this_seq_1 = "UUGGGGUUU"
#this_seq_2 = "UUGGGGUUC"
#type_of_point_mutation(this_seq_1, this_seq_2)

#this_seq_3 = "UUGUUC"
#this_seq_4 = "UUGUAC"
#type_of_point_mutation(this_seq_3, this_seq_4)

#this_seq_5 = "UUGUAC"
#this_seq_6 = "UUGUAA"
#type_of_point_mutation(this_seq_5, this_seq_6)

#this_seq_7 = "UUGGAU"
#this_seq_8 = "UUGGAU"
#type_of_point_mutation(this_seq_7, this_seq_8)

#list_files()

#file_path = "C:/Users/kmark/Documents/GitHub/CM515-2026/modules/wk_05_programming_2/independent_practice/fasta1.fa"
#extract_fasta_headers(file_path)