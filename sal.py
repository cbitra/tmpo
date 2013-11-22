#!/usr/local/bin/python

print("Enter the number of hours worked: ")
hours_worked = int(raw_input())

rate = 25.00

if hours_worked > 40:
    grosspay = (40 * rate) + ((hours_worked - 40) * (rate * 1.5))
else:
    grosspay = hours_worked * rate
print("Gross pay: " + str(grosspay)) 
