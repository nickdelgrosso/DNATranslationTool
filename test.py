import pytest
from main import *
from validation import validate_DNA_seq

cases = [
    ("ATG", "CAT"),
    ("GGCCTA","TAGGCC")
    ]
@pytest.mark.parametrize(["string", "complement"], cases)
def test_make_complement(string,complement):
    assert make_complement(string)==complement


cases = [
    ("ATG", "CAU"),
    ("GGCCTA","UAGGCC")
    ]
@pytest.mark.parametrize(["string", "complement"], cases)
def test_make_RNA(string,complement):
    assert make_RNA(string)==complement


cases = [
    ("AUG", ["Met"]),
    ("AUGGAA", ["Met", "Glu"])
    ]
@pytest.mark.parametrize(["string", "complement"], cases)
def test_get_codon(string,complement):
    assert get_codon_from_RNA(string)== complement



def test_validate_DNA_seq():
    with pytest.raises(ValueError):
        validate_DNA_seq('ATASDIWEFJSLDMA')