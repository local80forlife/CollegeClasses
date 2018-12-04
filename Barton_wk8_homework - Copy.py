#Characters: 65
#Letters: 32
#Consonants: 21
#Digits: 22
#spaces: 2
#Word Characters: 4
#Punctuation: 5

def main():
    try:
        userInput = "C:/Users/v-bartan/OneDrive/College/data.txt"
        
    except:
        print("ERROR: Unable to load file, please try again")

    userFile = open(userInput, 'r')
    divide_file(userFile, userInput)

#logic for dividing and function control
def divide_file(file, userInput):
    
    totalCount = {"vowels":0, "consonants": 0, "punctuation":0, "characters":0,
                  "spaces":0, "digits":0, "total" : 0}
    totalChar = 0
    fileLine = file.readline()
    while fileLine != "":
        fileLine = fileLine.rstrip("\n")
        totalChar += len(fileLine)
        count = count_char(fileLine)
        
        totalCount["vowels"] += count["vowels"]
        totalCount["consonants"] += count["consonants"]
        totalCount["punctuation"] += count["punctuation"]
        totalCount["characters"] += count["characters"]
        totalCount["spaces"] += count["spaces"]
        totalCount["digits"] += count["digits"]
        totalCount["total"] += count["total"]
        fileLine = file.readline()
        
    print_stats(totalCount, userInput)
        
#count spaces and return a string with no spaces
def count_char(fileLine):
    fileLine = fileLine.lower()
    counts = {"vowels":0, "consonants": 0, "punctuation":0, "characters":0,
              "spaces":0, "digits":0, "total": 0}
    vowels = 'aeiou'
    punctuation = '!~`^()_{}[]|\\;:\"\',.?'
    characters = '@#$%&+-=<>*/'

    #count spaces
    for char in fileLine:
        counts["total"] = len(fileLine)
        if char == vowels[vowels.find(char)]:
            counts["vowels"] += 1
        elif char == punctuation[punctuation.find(char)]:
            counts["punctuation"] += 1
        elif char == characters[characters.find(char)]:
            counts["characters"] += 1       
        elif char == " ":
            counts["spaces"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        else:
            counts["consonants"] += 1
    return counts

def print_stats(stats, userInput):
    nameIndex = userInput.rfind('/')

    print("Breakdown for user file: " + userInput[nameIndex+1:])
    print("Total file Length: " + str(stats["total"]))
    print("Spaces: " + str(stats["spaces"]))
    print("Word Characters: " + str(stats["characters"]))
    print("Punctuation: " + str(stats["punctuation"]))
    print("Digits: " + str(stats["digits"]))
    print("Consonants: " + str(stats["consonants"]))
    
main()

'''
One problem I had, i didn't strip the new line '\n' off the fileLine so the
.isdigit() would return false
'''
