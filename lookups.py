import json

# create lookup DNA dict
DNA_dict = {"A": "T",
            "T": "A",
            "G": "C",
            "C": "G"}

# import codons dict
with open('data/codons.json') as json_file:
    codons_dict = json.load(json_file)