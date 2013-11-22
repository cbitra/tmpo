#!/usr/local/bin/python

total = 0
count = 0
average = 0
num = 0

while True:
    print("Enter a number: ")
    num = float(raw_input())
    if num <= 0:
        break
    total = total + num
    count = count + 1
average = total / count
print("Average of the number is: " + str(average))
