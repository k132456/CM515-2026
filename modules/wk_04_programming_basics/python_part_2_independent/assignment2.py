### This script is where you should input your solutions in the designated areas only. There is a space at the bottom of the file to do your own code testing.
### Run grading.py to grade your assignment. You may run this script as many times as you'd like; I will grade your submissions myself with this exact script.



# This function takes an input list and an item, and adds the item to the beginning of the list.
def add_to_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    input_list.insert(0, item)
    

    ### YOUR CODE ABOVE HERE ###
    
    return input_list


# This function takes two input lists and combines them.
def merge_lists(list_1, list_2):

    ### YOUR CODE BELOW HERE ###

    list_1.extend(list_2)
    merged_list = list_1

    ### YOUR CODE ABOVE HERE ###

    return merged_list


# This function takes an input list and an item, and removes all copies of the item from the list.
def remove_from_list(input_list, item):

    ### YOUR CODE BELOW HERE ###

    input_list = [element for element in input_list if element != item]

    #for element in input_list:
        #input_list.remove(item)
    
    
    #for numbers in range(len(input_list)):
        #input_list.remove(item)


    #while x < 7:
    #print(x)
    #x = x + 1
    #print(x)

    ### YOUR CODE ABOVE HERE ###

    return input_list


# This function takes a numerical grade (e.g. 75.4), and returns True or False depending on whether that grade will earn a B (between 80 and 90)
def check_if_b_grade(grade):

    ### YOUR CODE BELOW HERE ###

    if 80 < grade < 90:
        print(True)
    else:
        print(False)
    

    ### YOUR CODE ABOVE HERE ###

    #I do not understand the return part of defining functions (def); if i comment this out or delete the 'is_b_grade' after return, the code executre properly, but with the is_b_grade still in there it fails
    #return is_b_grade


# This function takes a list of RNA codons, and uses a dictionary to return a list of the amino acid translations. If any codon is invalid (aka, not in the dictionary), return an empty list.
def get_protein_seq(list_of_codons):

    codon_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*", "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

    ### YOUR CODE BELOW HERE ###

    output_list = []
    for x in list_of_codons:
        codon_dict.get(x)
        output_list.append(x)
    
    print(output_list)
    


    ### YOUR CODE ABOVE HERE ###
    
    return output_list


# This function reads in a text file, and counts how many times the word of interest appears.
def count_word_in_file(file_path, word_of_interest):

    ### YOUR CODE BELOW HERE ###


    word_count = 0
    with open(file_path, "r") as file:
        for line in file:
            words = line.split()
            for each_word in words:
                if(each_word == word_of_interest):
                    word_count = word_count + 1
    print(word_of_interest, "appears", word_count, "times.")



    ### YOUR CODE ABOVE HERE ###

    return word_count


# This function takes a list of 3 column names, and a list of data for each column (each data list is the same length), then outputs a correctly-formatted CSV file "data.csv".
def create_data_file(column_names_list, column1_data, column2_data, column3_data):

    ### YOUR CODE BELOW HERE ###

    import csv
    rows = []
    for x in range(len(column1_data)):
        row = [column1_data[x], column2_data[x], column3_data[x]]
        rows.append (row)

    with open("data.csv", "w", newline= "") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(column_names_list)
        csvwriter.writerows(rows)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    ### YOUR CODE ABOVE HERE ###

# This function reads in a CSV file, "file2.csv", and outputs two new files: tav.csv contains ONLY entries with "Tav" as the technician, 
# and andre.csv contains ONLY antries with "Andre" as the technician. Look at file2.csv before writing code!
def filter_data():

    ### YOUR CODE BELOW HERE ###
    # Source - https://stackoverflow.com/a/25687769
# Posted by Burhan Khalid
# Retrieved 2026-02-16, License - CC BY-SA 3.0

#    import csv

#    with open("file2.csv", "r") as i, open("tav.csv", "w") as o:
#        r = csv.reader(i, delimiter='\t')
#        w = csv.writer(o, delimiter='\t')
#        for row in r:
#            if row[3] == "Tav":
#            w.write(row)


    
    
    
    print("\nReplace this with your code!\n")

    ### YOUR CODE ABOVE HERE ###



### TEST YOUR CODE DOWN HERE (IF YOU WANT TO) ###

#print(add_to_list([2, 3, 4], 10))

#list_1 = [1, 2, 3]
#list_2 = [4, 5, 6]
#merge_lists(list_1, list_2)
#print(list_1)
#merged_list = list_1
#print(merged_list)

#list_3 = [10, 11, 12, 10, 13, 14, 10, 15, 16, 10]
#print(list_3)
#print(remove_from_list(list_3, 10))

#check_if_b_grade(82)
#check_if_b_grade(71)

#my_codon_list = ["UUU", "UUC", "UUA"]
#get_protein_seq(my_codon_list)

#count_word_in_file("C:/Users/kmark/Documents/GitHub/CM515-2026/modules/wk_04_programming_basics/python_part_2_independent/colors.txt", "purple")


import csv

with open("file2.csv", "r") as file, open("tav.csv", "w", newline= "") as newfile:
    file2File = csv.reader(file, delimiter='\t')
    tavFile = csv.writer(newfile, delimiter='\t')
    for row in file2File:
        if row[3] == "Tav":
            newfile.writerow(row)