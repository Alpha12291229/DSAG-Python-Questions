# Write a program to prompt user to enter a time in HH:MM:SS format. 
# The program displays the time and it simulates the running of a clock. 
# You are only allowed to use the sleep function in the time module to implement this simulated clock program.

from time import sleep
from IPython.display import clear_output

#input and getting the hour, min and sec from the input
time_input = input("Please enter the time HH:MM:SS")
hour, mins, sec = map(int, time_input.split(':'))

#checking if time is valid
if hour> 24 or mins > 60 or sec > 60:
    print("Invalid Time entered")
else:
    
    #repeat forever
    while True:

        #clearing the line
        clear_output(wait=True)
        
        #formating the string
        currenttime= (f'{hour:02d}:{mins:02d}:{sec:02d}')

        print(currenttime)

        #increment seconds by 1
        sec = sec+1

        #sleep the program for 1 second
        sleep(1)

        # When each value reaches the max, it will reset and increment the next value
        if sec == 60:
            sec = 0
            mins = mins+1

        if mins == 60:
            mins =0
            hour = hour+1

        if hour ==24:
            sec=0
            mins=0
            hour=0