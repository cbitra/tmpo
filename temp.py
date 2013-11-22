#!/usr/local/bin/python

message = "The recommended activity is: "

print("Enter the current temperature: ")
temp = int(raw_input())

if temp > 80:
    message = message + "Volley ball."
elif temp >= 70:
    message = message + "Cricket."
elif temp >= 55:
    message = message + "Beach Volley."
elif temp >= 0:
    message = message + "Ping pong."
else:
    message = message + "Sitting by the fire."

print(message)

