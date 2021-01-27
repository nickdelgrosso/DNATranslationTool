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
    codons_dict = json.loads(json_file)

def make_complement(string):
    complement_strand = ""
    for element in string:
        complement_strand += DNA_dict[element]

    return(complement_strand[::-1])

def make_RNA(string):
    complement_strand = make_complement(string)
    return complement_strand.replace('T', 'U')

cases = [
    ("ATG", "CAT"),
    ("GGCCTA","TAGGCC")
    ]

cases2 = [
    ("ATG", "CAU"),
    ("GGCCTA","UAGGCC")
    ]


@pytest.mark.parametrize(["string", "complement"], cases)
def test_make_complement(string,complement):
    assert make_complement(string)==complement

@pytest.mark.parametrize(["string", "complement"], cases2)
def test_make_RNA(string,complement):
    assert make_RNA(string)==complement
