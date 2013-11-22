#!/usr/local/bin/python

message = "The recommended activity is "
print("Enter the temperature: ")
temp = int(raw_input())
if temp > 85:
    message = message + "swimming."
elif temp >= 70:
    message = message + "tennis."
elif temp >= 32:
    message = message + "golf."
elif temp >= 0:
    message = message + "dancing."
else:
    message = messae + "sitting by the fire."


print(message)

