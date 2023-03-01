# Find Top 10 most frequent words in text file 
# Remove punctuations and stopwords provided

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~“‘'''

#Reading in stop words into stop_words
stop_words=[]
with open(r"stop_words_english.txt",encoding="utf-8") as f:
    for name in f:
        stop_words.append(name.rstrip())
                
wordfreq={}
#Reading in book 4
with open(r"book_04.txt",encoding="utf-8") as f:
    for line in f: 
        for word in line.split():                  #split each word into a new line
            temp_word = ""                         #create a temporary string
            
            #checking the word for punctuations and removing them
            for letter in word:                    
                if letter not in punctuations:
                    temp_word += letter

            #making all words lowercase
            temp_word = temp_word.lower()
            word = word.lower()
                    
            #checking if the word with and without punctuations is not in the stop list
            if (temp_word not in stop_words) and (word not in stop_words): 

                #if the word is not in dictionary, create with word as key and 0 as value
                if temp_word not in wordfreq:
                    wordfreq[temp_word] = 0
                    
                #add value of word by 1
                wordfreq[temp_word] += 1

#Sorting dictionary by descending order of value(count of words)
wordfreq=sorted(wordfreq.items(), key=lambda x: x[1], reverse=True)

#printing top 10 words
for x in (wordfreq[:10]):
    print(f'{x[0]} {x[1]}')
