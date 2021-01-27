## This python file will take a string of DNA letters and do something with it
import pytest
import json

# create lookup DNA dict
DNA_dict = {"A":"T",
            "T":"A",
            "G":"C",
            "C":"G"}

# import codons dict
with open('data/codons.json') as json_file:
    codons_dict = json.load(json_file)

def make_complement(string):
    complement_strand = ""
    for element in string:
        complement_strand += DNA_dict[element]

    return(complement_strand[::-1])

def make_RNA(string):
    complement_strand = make_complement(string)
    return complement_strand.replace('T', 'U')

def find_start_codon(rna_string):
    startcodon = []
    for i in range(rna_string.count("AUG")):
        startcodon.append(startcodon_index = rna_string.rfind("AUG"))

    return startcodon


def get_codon_from_RNA(RNA_string):
    codon_list = []
    for i in range(0,len(RNA_string),3):
        codon_list.append(RNA_string[i:i+3])
    amino_acid_list = []
    for codon in codon_list:
        amino_acid_list.append(codons_dict[codon])
    return amino_acid_list



