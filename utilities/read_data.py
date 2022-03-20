import csv
import json
from configparser import ConfigParser


def get_csv_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    print("rr" + str(reader))
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    print(rows)
    return rows


def readconfig(file_name):
    config = ConfigParser()
    config.read("./configfiles/" + file_name + ".cfg")
    return config


def read_csv_data(file_name):
    # open the CSV file
    data_file = open("./testData/" + file_name, "r")
    # create a CSV Reader from CSV file
    reader = csv.DictReader(data_file)
    list_data = list(reader)
    # return reader
    return list_data


def read_json_file(file_name: str) -> json:
    with open(f"./test_data/{file_name}", "r") as json_file:
        data = json.load(json_file)
        return data
