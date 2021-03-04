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

def find_prefix(num):
    if num[:3] == "140": #Telemarketer numbers
        prefix = 140
    elif num[0] == "(": #Landlines
        prefix = num.split(")")[0].strip("(") #could use regex here
    elif " " in num: #Mobile numbers, check these last
        if num[0] in {"7", "8", "9"}:
            prefix = num[:4]
        else:
            return "ERROR: Invalid mobile number"
    else:
        return "ERROR: No prefix found"
    assert(type(prefix) == str)
    return prefix

def find_prefixes_for_bangs(file):
    prefixes = set()
    for record in file:
        caller = record[0]
        if caller[:5] == "(080)":
            callee = record[1]
            prefix = find_prefix(callee)
            prefixes.add(prefix)
    prefixes = sorted(list(prefixes))
    return(prefixes)

def find_perc_bang(file):
    calls_to_bang = 0
    calls_to_other = 0
    for record in file:
        caller = record[0]
        if caller[:5] == "(080)":
            receiving = record[1]
            if receiving[:5] == "(080)":
                calls_to_bang += 1
            else:
                calls_to_other += 1
    total_calls_from_bang = calls_to_bang + calls_to_other
    ratio = calls_to_bang / total_calls_from_bang
    percentage = round(ratio, 4) * 100
    return percentage

prefixes = find_prefixes_for_bangs(calls)
print("The numbers called by people in Bangalore have codes:")
for prefix in prefixes:
    print(prefix)

perc = find_perc_bang(calls)
print(f"\n{perc} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
