import os
import json


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def read_data(infile):
    with open(infile, "r") as file:
        data = json.loads(file)
    return data


def write_data(data_dict, outfile):
    with open(outfile, "w") as file:
        json.dumps(data_dict, file)
