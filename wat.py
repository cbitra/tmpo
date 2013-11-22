#!/usr/local/bin/python

response = "chandra"
tries = 0

while(tries <= 3):
    print("Enter the name of the person who played with the computer: ")
    response = raw_input()
    tries = tries + 1

    if (response == "chandra"):
         print("chandra is the correct answer")
         break;
    elif (tries == 3):
         print("Sorry ! you have tried 3 times")
         break;
    else:
        print("You have another chance to try")



