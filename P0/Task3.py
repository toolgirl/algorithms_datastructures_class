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

# Part A:
def get_numbers(calls):
    numbers_called = []
    # Get the first 5 digits of numbers called from Bangalore.
    for line in calls:
        if line[0][:5] == "(080)":
            numbers_called.append(line[1])
    return numbers_called


def get_sorted_area_codes():
    numbers = get_numbers(calls)
    area_codes = []
    for number in numbers:
        if number[0] == "7" or number[0] == "8" or number[0] == "9":
            area_codes.append(number[:4])
        if number[:3] == "140":
            area_codes.append("140")
        if number[0] == "(":
            num = []
            for digit in number:
                num.append(digit)
                if digit == ")":
                    area_codes.append(''.join(num))
                    break
    return sorted(area_codes)


def pretty_print_codes():
    # Run the functions to get the data and print it out.
    sorted_codes = set(get_sorted_area_codes())
    print("The numbers called by people in Bangalore have the following codes:")
    for code in sorted_codes:
        print(code)


pretty_print_codes()


# Part B:
def get_local_calls_stats():
    numbers_called = get_sorted_area_codes()
    total = len(numbers_called)
    local_count = 0
    for n in numbers_called:
        if n == '(080)':
            local_count += 1
    local_percent = round((local_count / total) * 100, 2)
    return "{} percent of calls from land lines in Bangalore are calls to other land lines in Bangalore.".format(local_percent)


print(get_local_calls_stats())


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
