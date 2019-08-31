def is_leap_year(year):
#     The year is evenly divisible by 4;
#     If the year can be evenly divided by 100, it is NOT a leap year, unless;
#     The year is also evenly divisible by 400. Then it is a leap year.
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def date1BeforeDate2(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysInMonth(year, month):
    # Returns the number of days in a month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year):
        months[1] = 29
    return months[month - 1]

def nextDay(year, month, day):
    #Returns the next day after the day given
    days_in_month = daysInMonth(year, month)
    if day < days_in_month:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
        Calculates the number of days between two dates, assuming a valid date in the Gregorian Calendar as imput.
    """
    assert not date1BeforeDate2(year2, month2, day2, year1, month1, day1)
    days = 0
    while date1BeforeDate2(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
#TESTS
def test():
    # test same day
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 2018, 1, 1) == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29) == 365)
    #test leap year 2
    assert(is_leap_year(2004) == True)
    #test leap year 0
    assert(is_leap_year(2000) == True)
    #test leap year 1
    assert(is_leap_year(2020) == True)
    # test not leap year
    assert(is_leap_year(2017) == False)
    # test not leap year
    assert(is_leap_year(2011) == False)
    #test not leap year 1
    assert(is_leap_year(1900) == False)
    #test daysInMonth
    assert(daysInMonth(1999, 1) == (31))
    assert(daysInMonth(2013, 2) == (28))
    assert(daysInMonth(2020, 2) == (29))
    assert(daysInMonth(2012, 3) == (31))
    assert(daysInMonth(2020, 4) == (30))
    assert(daysInMonth(2000, 5) == (31))
    assert(daysInMonth(2000, 2) == (29))
    assert(daysInMonth(1900, 6) == (30))
    assert(daysInMonth(1904, 7) == (31))
    assert(daysInMonth(1977, 8) == (31))
    assert(daysInMonth(2010, 9) == (30))
    assert(daysInMonth(2011, 10) == (31))
    assert(daysInMonth(2014, 11) == (30))
    assert(daysInMonth(2017, 12) == (31))
    # Test nextDay
    assert(nextDay(1999, 12, 31) == (2000, 1, 1))
    assert(nextDay(2013, 1, 31) == (2013, 2, 1))
    assert(nextDay(2012, 12, 31) == (2013, 1, 1))
    assert(nextDay(2012, 2, 29) == (2012, 3, 1))
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

test()
