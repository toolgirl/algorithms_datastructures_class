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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def format_head(texts):
    # Check records has the right format
    assert len(texts[0]) == 3
    in_num, aws_num, time = texts[0]
    first_text = "First record of texts, {} texts {} at time {}".format(in_num, aws_num, time)
    return first_text

def format_tail(calls):
    # Check records has the right format
    assert len(calls[-1]) == 4
    in_num, aws_num, time, duration= calls[-1]
    last_call= "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(in_num, aws_num, time, duration)
    return last_call

print(format_head(texts))
print(format_tail(calls))

