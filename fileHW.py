# Hello world dot py

import random
import sys
import os

print("Hello, \n What\'s your name?\n" "")
name01 = input("enter response: \n"   "")
print("Hi "+ name01 +" my name is Hal.\n")
print("\n How are you feeling today?\n" "")
feel01 = input("Good or Bad: \n" "")
if feel01 == 'Good' :
        print("I'm glade to hear that!\n Oh\' I\'m sorry I\'ve got to go computer stuff to do.\n It was nice meeting you...\nBye!")
elif feel01 == 'Bad' :
        input("That\'s not good. Do you want to talk about it?\n" "yes - no:\n " "")

else:
        print("Sorry I got to go.")
