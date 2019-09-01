
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
    distinct_num = set()
    for row in data:
        distinct_num.add(row[0])
        distinct_num.add(row[1])
    return "There are {} different telephone numbers in the records.".format(len(distinct_num))


print(get_number_count(calls, texts))
'''
Big O:
O(n)
'''