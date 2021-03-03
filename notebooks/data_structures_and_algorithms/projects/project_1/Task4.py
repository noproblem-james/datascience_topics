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

def find_suspects(texts_file, calls_file):
    suspects = set()
    whitelist = set()
    for line in texts_file:
        sender = line[0]
        recipient = line[1]
        whitelist.add(sender) #telemarketers never send texts
        whitelist.add(recipient) #telemarketers never receive texts
    for line in calls_file:
        caller = line[0]
        callee = line[1]
        whitelist.add(callee) #telemarketers never receive calls
        if callee in suspects:
            suspects.remove(callee)
        if caller not in whitelist:
            suspects.add(caller)
    suspects = list(sorted(suspects))
    return suspects

suspects = find_suspects(texts_file=texts, calls_file=calls)

print("These numbers could be telemarketers:")
for suspect in suspects:
    print(suspect)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

