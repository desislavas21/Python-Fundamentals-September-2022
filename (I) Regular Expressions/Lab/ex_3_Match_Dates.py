# Write a program, which matches a date in the format "dd{separator}MMM{separator}yyyy". Use capturing groups in your regular expression.
# Compose the Regular Expression
# Every valid date has the following characteristics:
# •	It always starts with two digits, followed by a separator
# •	After that, it has one uppercase and two lowercase letters (e.g., Jan, Mar).
# •	After that, it has a separator and exactly 4 digits (for the year).
# •	The separator could be one of these symbols: a period ("."), a hyphen ("-") or a forward-slash ("/").
# •	The separator must be the same for the whole date (e.g., 13.03.2016 is valid, 13.03/2016 is NOT). Use a group backreference to check for this.
# Input
# 13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016
# Output
# Day: 13, Month: Jul, Year: 1928
# Day: 10, Month: Nov, Year: 1934
# Day: 25, Month: Dec, Year: 1937

import re
dates = input()
patters = r"\b(\d{2})([\-\.\/])([A-Z][a-z]{2})\2(\d{4})\b"
all = re.findall(patters, dates)
for date in all:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[-1]}")