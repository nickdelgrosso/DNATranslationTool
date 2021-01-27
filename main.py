## This python file will take a string of DNA letters and do something with it
import pytest

# create lookup DNA dict
DNA_dict = {"A":"T",
            "T":"A",
            "G":"C",
            "C":"G"}


def make_complement(string):
    complement_strand = ""
    for element in string:
        complement_strand += DNA_dict[element]

    return(complement_strand)


cases = [
    ("ATG", "TAC"),
    ("GGCCTA","CCGGAT")
    ]

@pytest.mark.parametrize(["string", "complement"], cases)
def test_make_complement(string,complement):
    assert make_complement(string)==complement