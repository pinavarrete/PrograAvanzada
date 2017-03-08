import csv


def lector_csv(path):
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter= ',')
        for line in reader:
            yield line
