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

#This is the countdown function that will take the seconds(t) and countdown until the times is at 0.
#Using the format method it will format it into minutes:seconds.
#Every second of the loop that passes it will update the timer variable with the new value.
#
def countdown(t):

    while t:
        #divmod is just dividing divmod(dividend, divisor).
        #Here it is dividing 1 by 60, for every 60 seconds it adds one to the min variable.
        mins, secs = divmod(t, 60)
        #This is the timer variable that is using .format to put it into minutes and seconds.
        #the colon (:) is adding spaces before each of the numbers.
        #02d is just a placeholer that is replaced by the parameters of .format().
        timer = '{:02d}:{:02d}'.format(mins, secs)
        #This is printing the current time left, and overwriting the line each time to display the current time left.
        print(timer, end='\r')
        #Time sleep is just adding a pause that last the number of seconds put in the parameters.
        time.sleep(1)
        #This is subtracting 1 from the t variable to eventually get to 0.
        #Where t is represented as the number of seconds determined by the user.
        t -= 1

    print("Time is up.")

#The variable(t) is defined by the user's input when given the prompt. 
t = input("Enter the time in seconds: ")

#This calls the countdown function, then converts the string t into and integer.
#The value stored in (t) is then used as the value that will be kicked into the function.
countdown(int(t))
