#!/usr/local/bin/python

print("Enter your percentage: ")
percentage = int(raw_input())

if percentage >= 80:
    grade = "A"
elif percentage >= 65:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 35:
    grade = "D"
elif percentage <= 34:
    grade = "F"
else:
    print("Enter your percentage: ")

print("Your grade is = " + grade )

