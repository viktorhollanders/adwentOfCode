import csv

list_1 = []
list_2 = []

input_file = "puzzle_input/day1_data.csv"

with open(input_file, mode="r") as file:
    csvreader = csv.reader(file, delimiter=";")

    header = next(csvreader)
    col1_index = header.index("col1")
    col2_index = header.index("col2")

    for row in csvreader:
        list_1.append(int(row[col1_index]))
        list_2.append(int(row[col2_index]))


list_1.sort()
list_2.sort()

list_distance = 0
i = 0


while i < len(list_1):
    if list_1[i] > list_2[i]:
        list_distance += list_1[i] - list_2[i]
        i += 1
    else:
        list_distance += list_2[i] - list_1[i]
        i += 1

print(list_distance)

similarity_score = 0

for num1 in list_1:
    count = 0
    for num2 in list_2:
        if num1 == num2:
            count += 1
    similarity_score += count * num1

print(similarity_score)
