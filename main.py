## This python file will take a string of DNA letters and do something with it
import pytest

complement_strand= ""
def make_complement(string):
    for element in string:
        complement_strand.append(element)


cases = []
    ("ATG",  )
]

@pytest.mark.parametrize("string,complement", cases)
def test_make_complement(string,complement):
    assert make_complement(string)==complement