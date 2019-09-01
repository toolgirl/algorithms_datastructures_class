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
def get_telemarketers(calls, texts):
    outgoing_num = set(line[0] for line in calls)
    receiving_num = set(line[1] for line in calls)
    for row in texts:
        receiving_num.add(row[0])
        receiving_num.add(row[1])
    telemarketers = outgoing_num - receiving_num
    print("These numbers could be telemarketers: ")
    for number in sorted(telemarketers):
        print(number)

#

get_telemarketers(calls, texts)