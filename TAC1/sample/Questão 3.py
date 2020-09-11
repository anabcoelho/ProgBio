import csv
with open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados\\species.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[3].upper().rstrip() == "BIRD":
            print (row)