import csv

with open ('biostats.csv','r',newline='') as biostats:
    lector_csv = csv.reader(biostats)
    for fila in lector_csv:
        print(fila)
