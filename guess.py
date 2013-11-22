#!/usr/local/bin/python

import os
os.system('clear')

answer = "Watson"
print("Let us play a game.")
print("What is the name of the computer that played on Jeopardy ? ")
response = raw_input()

if response == answer:
    print("That is correct")
else:
    print("Sorry ! Guess again : ")
    response = raw_input()
    if response == answer:
        print("That is right!")
    else:
        print("Sorry ! Guess again: ")
        response == raw_input()
        if response == answer:
            print("That is correct.")
        else:
            print("Sorry !  No more tries.  The correct answer is " + answer )

