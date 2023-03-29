import csv

with open('countries.csv', 'r') as file_open:
    data = csv.reader(file_open)
    data = list(data)
    print(data)

with open('countries.csv', 'r') as fp:
    data = list(csv.DictReader(fp, delimiter=','))
    print(data)
