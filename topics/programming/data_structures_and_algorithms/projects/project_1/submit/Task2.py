"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def count_duration(file):
    duration_dict = {}
    for line in file:
        caller = line[0]
        callee = line[1]
        duration = line[3]
        for num in [caller, callee]:
            total = duration_dict.get(num, 0)
            total += float(duration)
            duration_dict[num] = total
    return duration_dict

def find_longest_total(duration_dict):
    phone_num, longest_duration = None, 0
    for k, v in duration_dict.items():
        if v > longest_duration:
            longest_duration = v
            phone_num = k
    return phone_num, longest_duration

phone_num, longest_duration = find_longest_total(count_duration(calls))
print(f"{phone_num} spent the longest time, {longest_duration} seconds, on the phone during September 2016.")



