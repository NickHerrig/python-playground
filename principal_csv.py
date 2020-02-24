import csv

with open('principal-csv.csv', newline='') as file:
    data = csv.reader(file, delimiter=',')
    headers = next(data)
    solutions = []
    for row in data:
        if row[0] == 'addition':
            solutions.append(int(row[1]) + int(row[2]))
        elif row[0] == 'multiplication':
            solutions.append(int(row[1]) * int(row[2]))
        elif row[0] == 'division':
            solutions.append(int(row[1]) / int(row[2]))
        elif row[0] == 'subtraction':
            solutions.append(int(row[1]) - int(row[2]))
        print(row, solutions[-1])
        

#operation,num1,num2
#addition,52,6584
#subtraction,168,73
#multiplication,22,7
#division,1362,40
