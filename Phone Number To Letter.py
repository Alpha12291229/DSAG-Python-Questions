# Each number on the telephone dial (except 0 and 1) corresponds to three alphabetic characters. For example 2 corresponds to abc, 3 corresponds to def and etc.
# Write a function named num_name(). It prompts user to enter a 8 digits telephone number and prints out all combination of words. 
# If the phone number contains 0 or 1, it prints a message "Invalid phone number for words".
# You are required to implement the solution using a nested list data structure. 

def num_name(phone_number):
    
    #phone number to alphabet
    correspond = [[],[],['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
    
    #changing inputted phone number to a list of integers
    number = list(map(int,phone_number))
    
    #Checking if the number contains 1 or 0
    for i in number:
        if i == (0 or 1):
            print ("Invalid phone number for words")
            return
        
    #Getting all characters of the last digit
    combinations = [str(ch) for ch in correspond[number[-1]]]

    #Starting from the 2nd last digit
    for i in range(len(number)-1, 0,-1):

        #append each complete character into the list
        prevList = combinations.copy()
        combinations = [ ch +s for ch in correspond[number[i-1]] for s in prevList]

    #print output list with all the combinations
    print(*combinations, sep = "\n")
         
num_input = input("Enter a phone number please: ")
num_name(num_input)