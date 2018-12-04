#Andrew Barton - CSC 110 wk8 Homework - 11/27/18
#This program takes in a file location from user and breaks down the contents
#to count and print the contents of the file

#Loop the program unit user enters 'q' or 'Q', send file location to divid_file
#to break it down
def main():
    userInput = ''
    while userInput != 'q':
        userInput = input("Enter the File Location: ")
        userInput = userInput.lower()
        if userInput == 'q':
            break
        else:
            divide_file(userInput)
    
#opens the file and sends each line to each funtion to return the counts. After
#counts are collected and summed up send to the print function
def divide_file(userInput):
    #Have to create varaibles before adding the first counts
    totalChar = 0
    space = 0
    wordChar = 0
    puncChar = 0
    digit = 0
    letter = 0
    vowel = 0
    try:
        userFile = open(userInput, 'r')
        fileLine = userFile.readline()
        while fileLine != "":
            totalChar += len(fileLine)          #Counting total characters
            space += find_space(fileLine)       #Counting spaces
            wordChar += find_wordChar(fileLine) #Counting word characters
            puncChar += find_punc(fileLine)     #Counting Punctuation 
            digit += find_digit(fileLine)       #Counting numbers
            letters = find_letter(fileLine)     #Returns dictionary
            vowel += letters["Vowels"]          #From dictionary count vowels
            letter += letters["Letters"]        #From dictionary count consonant
            fileLine = userFile.readline()
        userFile.close()
        print_stats(totalChar, space, wordChar, puncChar, digit, letter, vowel,
                        userInput)
    except: #if file can't load
        print("ERROR: Unable to load the file, please try again")
 
#function counts the spaces and returns the count of one line at a time
def find_space(fileLine):
    spaceCount = 0 
    for char in fileLine:
        if char == " ":
            spaceCount += 1
        elif char == "\t":
            spaceCount += 1
        elif char == "\n":
            spaceCount += 1
    return spaceCount

#function counts the word characters and returns the count of one line at a time
def find_wordChar(fileLine):
    wordCharCount = 0
    characters = '@#$%&+-=<>*/'
    for char in fileLine:
        if char == characters[characters.find(char)]:
            wordCharCount += 1
    return wordCharCount

#function counts punctuation characters one line at a time and return count 
def find_punc(fileLine):
    puncCount = 0
    punctuation = '!~`^()_{}[]|\\;:\"\',.?'
    for char in fileLine:
        if char == punctuation[punctuation.find(char)]:
            puncCount += 1
    return puncCount
    
#function counts digits one line at a time and return count
def find_digit(fileLine):
    digitCount = 0
    for char in fileLine:
        if char.isdigit():
            digitCount += 1
    return digitCount
            
#function counts vowels and consonants and returns a dictionary with counts
def find_letter(fileLine):
    fileLine = fileLine.lower()
    letters = {"Letters" : 0, "Vowels": 0}
    letterCount = 0
    vowelCount = 0
    vowels = 'aeiou'
    for char in fileLine:
        if char.isalpha():
            if char == vowels[vowels.find(char)]:
                vowelCount += 1
                continue
            else:
                letterCount += 1
    letters["Letters"] = letterCount
    letters["Vowels"] = vowelCount
    return letters   

#function takes all the counts from divide_file and prints the numbers
def print_stats(totalChar, space, wordChar, puncChar, digit, letter, vowel,
                userInput):
    print("\n")
    print("Source File: " + userInput)
    print("Total file Length: {:_>3}".format(str(totalChar))) #includes '\n'
    print("Spaces: {:_>14}".format(str(space)))
    print("Word Characters: {:_>5}".format(str(wordChar)))
    print("Punctuation: {:_>9}".format(str(puncChar)))
    print("Digits: {:_>14}".format(str(digit)))
    print("Letters: {:_>13}".format(str(letter + vowel)))
    print("Consonants: {:_>10}".format(str(letter)))
    print("\n")
    
main()

'''
I was wrote it the first time thinking it would be effective to remove the
characters as I counted them. Thinking that as is moved on to the next function
it would be a shorter string so it would be a faster process. I was talking to
a software engineer and he was telling me to be efficient I need to cut down on
the number of times it would run through the file line. So I rewrote it to run
in one function not removing any characters and just having everything count at
one time. After I got it to run I looked at the homework write up again and saw
you wanted a function for each character counting. I wrote everything again as
so everything has its function and without removing characters . But doing all
this was very helpful to see different errors, for instance I was using
.isdigit() to check a full file line was digits and even if my test file was
only digits it was always returning false cause I forgot to remove the ’\n’
from the file lines 

to test I had a .py file and .txt file with the same text, for some lines like
the .isidgit() problem I talked about above I created local variables to test
it, so I figure could out the '\n' was the issue

I would like a program of find something I can paste my code into and see how
effctive it is, which one of my copies works better then the other. Next I think
learning GUI would be cool and the use of buttons



'''




































































'''
