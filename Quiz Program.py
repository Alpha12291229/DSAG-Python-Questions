# Randomise Questions and answer choices 
# Show 1 of 3 congratulatory phrase if correct
# Show correct answer if wrong
# Show Score at the end of the quiz

# Quiz CSV file details:
# Each Question has 4 answers 
# 1st answer is always correct

import random

# Reading in the file
words=[]
with open(r"quiz.csv",'r') as f:
    for name in f:
        words.append(name.rstrip())

questionlist = []
answerlist =[]
correct_string = ["Good job!","Awesome!", "Correct!"]
options = ["a","b","c","d"]

no_questions = int(len(words)/5)              #Number of questions in the list
for i in range(no_questions):
    questionlist.append(words[i*5])           #makes the list of questions            
    answerlist.append(words[(i*5)+1:(i*5)+5]) #makes the nested list of answers
    
#Shuffle the questionlist and answerlist using shuffling function
templist = list(zip(questionlist, answerlist))
random.shuffle(templist)
questionlist, answerlist = map(list,zip(*templist))

correct_counter = 0
for i in range(no_questions):                                  #for each question:
    correct_ans = answerlist[i][0]                             #save the correct answer
    random.shuffle(answerlist[i])                              #shuffle the order of the options
    correct_index = options[answerlist[i].index(correct_ans)]  #change correct answer to correct corresponding letter

    print(f"\nQuestion {str(i+1)}")                          #printing the question number
    print(f"{questionlist[i]}")                              #printing the question
    for x in range(4):                                       #printing the options
        print(f'{options[x]}.{answerlist[i][x]}')               
    
    input_ans=input()
    if (correct_index == input_ans):                                                       #if correct:
        print(random.choice(correct_string))                                               #prints 1 out of 3 phrases
        correct_counter +=1                                                                #increase correct countercounter 
    else: print(f'Sorry, you selected a wrong option, the correct ans is {correct_index}') #else print correct answer
        
correct = round((correct_counter/no_questions*100),2)    #Cacluating score
print(f'\nEnd of the Quiz. You Scored {correct}')
