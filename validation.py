from lookups import DNA_dict

def validate_DNA_seq(DNA_string):
    for N in DNA_string:
        if N not in DNA_dict.keys():
            raise ValueError("Wrong nucletide character")

