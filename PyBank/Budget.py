from operator import itemgetter

# Importing the os module will allow for the creation of a file paths across operating systems
import os


# Then we must import the module for reading CSV files
import csv

with open('budget_data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    data= []
    for row in csv_reader:
        data.append(row)

headers = data.pop(0)
sorted_list = sorted(data, key=itemgetter(1))
output_data = 'Total Months: {}\nSum Months: ${}\nAverage Change: ${}\nGreatest Increase: ${}\nGreatest Decrease: ${}'.format(
    len(sorted_list),                                           # Total Months
    sum([int(row[1]) for row in data]),                         # Total Sum
    sum([int(row[1]) for row in data])/len(sorted_list),        # Average
    sorted_list[-1],                                            # Greatest Increase
    sorted_list[0]                                              # Greatest Decrease
)

print(output_data)

outputname = 'output.txt'

with open(outputname, 'w') as f:
    f.write(output_data)

    print('File written: {}'.format(outputname))
