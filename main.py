"""
    Countdown timer 
    June 18th 2025

    1.) Allow the user to input the time
    2.) Count down to 0
    3.) Tell the user that the time is up.

    Im thinking that there is going to have to be some kind of for loop.
    Will this timer countdown in minutes and seconds or just seconds?
"""

import time

#I borrowed this from an example. I am working on figuring out how it works.
def countdown(t):

    while t:
        #divmod is just dividing divmod(dividend, divisor)
        mins, secs = divmod(t, 60)
        #I am not sure what the {:02d} is. It is more than likely the formating for the time.
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #This is printing the current time left, and overwriting the line each time to display the current time left.
        print(timer, end='\r')
        #I need to look more into the sleep function.
        time.sleep(1)
        #This is subtracting 1 from the t variable to eventually get to 0.
        t -= 1

    print("Time is up.")


t = input("Enter the time in seconds: ")

countdown(int(t))
