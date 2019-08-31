from collections import defaultdict
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def get_longest_call(calls):
    # Create and populate a defaultdict with phonenumbers and call times.
    phonenumbers = defaultdict(list)
    for call in calls:
        phonenumbers[call[0]].append(int(call[-1]))
        phonenumbers[call[0]].append(int(call[-1]))
    call_times = {k:sum(v) for k,v in phonenumbers.items()}
    max_key = max(call_times, key=call_times.get)
    return "{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, call_times[max_key])

print(get_longest_call(calls))
