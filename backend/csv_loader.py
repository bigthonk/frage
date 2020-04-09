import csv
import json

with open('movies.csv') as f:
    a = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]
    with open('movies.json', 'w') as json_file:
        json.dump(a, json_file)
