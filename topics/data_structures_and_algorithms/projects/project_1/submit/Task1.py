"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_tel_nums(files):
    res_set = set()
    for file in files:
        for line in file:
            res_set.add(line[0])
            res_set.add(line[1])
            count = len(res_set)
    return count

num_count = count_tel_nums([texts, calls])

print(f"There are {num_count} different telephone numbers in the records." )

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
