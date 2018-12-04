#Characters: 65
#Letters: 32
#Consonants: 21
#Digits: 22
#spaces: 2
#Word Characters: 4
#Punctuation: 5

totalChar = 0
spaceCount = 0
wordCharCount = 0
puncCharCount = 0
digitCount = 0
letterCount = 0
vowelCount = 0;

def main():
    try:
        userInput = "C:/Users/v-bartan/OneDrive/College/data.txt"
        
    except:
        print("ERROR: Unable to load file, please try again")

    userFile = open(userInput, 'r')
    divide_file(userFile)
    print_stats()

#logic for dividing and function control
def divide_file(file):
    global totalChar
    fileLine = file.readline()
    while fileLine != "":
        fileLine = fileLine.rstrip("\n")
        totalChar += len(fileLine)
        noSpaces = find_space(fileLine)
        noWordChar = find_wordChar(noSpaces)
        noPuncChar = find_punc(noWordChar)
        noDigits = find_digit(noPuncChar)
        find_letter(noDigits)
        fileLine = file.readline()
        
#count spaces and return a string with no spaces
def find_space(fileLine):
    global spaceCount #allow global variable to be assigned locally
    noSpaceString = fileLine
    #count spaces
    for char in fileLine:
        if char == " ":
            spaceCount += 1 #add to the global variable
        else:
            continue    
    #remove spaces from the fileLine and return to divide_file with no spaces
    noSpaceString = noSpaceString.replace(" ", "")
    return noSpaceString

#count word characters and return a string with no characters
def find_wordChar(fileLine):
    global wordCharCount #allow global variable to be assigned locally
    noWordCharString = fileLine
    characters = ['@','#','$','%','&','+','-','=','<','>','*','/']
    #count word characters by comparing them to the list of characters
    for fileChar in fileLine:
        for wordChar in characters:
            if fileChar == wordChar:
                wordCharCount += 1 #add to the global variable
                #remove characters
                noWordCharString = noWordCharString.replace(fileChar, "")
            else:
                continue
    #remove characters from the fileLine(noSpaces) return to divide_file
    return noWordCharString

#count punctuation and move to a seperate string
def find_punc(fileLine):
    global puncCharCount #allow global variable to be assigned locally
    noPuncString = fileLine
    punctuation = ['!', '~', '`', '^', '(', ')', '_', '{', '}', '[', ']', '|',
                   '\\', ';', ':', '\"', '\'', ',', '.', '?']
    for fileChar in fileLine:
        for puncChar in punctuation:           
            if fileChar == puncChar:
                puncCharCount += 1 #add to the global variable
                noPuncString = noPuncString.replace(fileChar, "")
            else:
                continue
    return noPuncString
    
#count digits and move to a seperate string
def find_digit(fileLine):
    global digitCount #allow global variable to be assigned locally
    noDigitsString = fileLine
    allDigit = fileLine.isdigit()

    if allDigit == True:
        digits = len(fileLine)
        digitCount += digits
        noDigitsString = ""
    else:
        for num in noDigitsString:
            if num.isdigit():
                digitCount += 1
                noDigitsString = noDigitsString.replace(num, "")
    return noDigitsString
            

#find vowels, count, and subtract from the remaining string
def find_letter(fileLine):
    global letterCount
    global vowelCount
    fileLine = fileLine.lower()
    
    allLetters = 0
    vowels = ['a','e','i','o','u']
    if fileLine != "":
        allLetters = len(fileLine)
        letterCount += allLetters
        for letter in fileLine:
            for vowel in vowels:
                if letter == vowel:
                    vowelCount += 1
            

def print_stats():
    global letterCount
    global vowelCount

    letterCount = letterCount - vowelCount
    print("Total file Length: " + str(totalChar))
    print("Spaces: " + str(spaceCount))
    print("Word Characters: " + str(wordCharCount))
    print("Punctuation: " + str(puncCharCount))
    print("Digits: " + str(digitCount))
    print("Consonants: " + str(letterCount))
    
main()

'''
One problem I had, i didn't strip the new line '\n' off the fileLine so the
.isdigit() would return false
'''
