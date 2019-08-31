from collections import Counter
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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_number_count(calls, texts):
    data = calls + texts
    print(len(data))
    distinct_num = Counter()
    for line in data:
        distinct_num.update(line[:2])
    return "There are {} different telephone numbers in the records.".format(len(distinct_num))

print(get_number_count(calls, texts))