#! Calendar Module
# The calendar module allows you to output calendars and provides
# additional useful functions for them.
# class calendar.TextCalendar([firstweekday])
# This class can be used to generate plain text calendars.
# Example:
# >>> import calendar
# >>>
# >>> print calendar.TextCalendar(firstweekday=6).formatyear(2015)
#
# Task:
# You are given a date. Your task is to find what the day is on that date.
#
# Input Format:
# A single line of input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.
#
# Output Format:
# Output the correct day in capital letters.
#
# Sample Input:
# 08 05 2015
# Sample Output:
# WEDNESDAY
#
# Explanation:
# The day on August th  was WEDNESDAY.

import calendar

month, day, year = map(int, (input().split()))
print(calendar.day_name[calendar.weekday(year, month, day)].upper())