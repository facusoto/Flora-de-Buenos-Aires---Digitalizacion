import re
import csv

file1 = open(file="output.txt", mode="r", encoding="utf-8")
content = file1.readlines()
counts = dict()
line_count = 0

tabulation = '\t'

for line in content:
    line_count += 1
    if tabulation in line:
        counter = line.count(tabulation)
        counts[line_count] = counter
    else:
        counts[line_count] = 0

print("finalizado")

file_object = open('tabs_in_file.csv', mode='w', encoding='utf-8', newline="")
writer = csv.writer(file_object, delimiter = ",")
for key, value in counts.items():
    writer.writerow([key, value])