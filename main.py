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

def get_codon_from_RNA(RNA_string):
    codon_list = []
    for i in range(0,len(RNA_string),3):
        RNA_string[i:i+3]

cases_DNA_complement = [
    ("ATG", "CAT"),
    ("GGCCTA","TAGGCC")
    ]

cases_DNAtoRNA = [
    ("ATG", "CAU"),
    ("GGCCTA","UAGGCC")
    ]
cases_codon_from_RNA = [
    ("AUG", "Met")
    ("AUGGAA", ["Met", "Glu"])
    ]

@pytest.mark.parametrize(["string", "complement"], cases_DNA_complement)
def test_make_complement(string,complement):
    assert make_complement(string)==complement

@pytest.mark.parametrize(["string", "complement"], cases_DNAtoRNA)
def test_make_RNA(string,complement):
    assert make_RNA(string)==complement

@pytest.mark.parametrize(["string", "complement"], cases_codon_from_RNA)
def test_get_codon(string,complement):
    assert get_codon_from_RNA(string)== complement