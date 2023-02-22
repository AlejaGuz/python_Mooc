import string

listLetters = list(string.ascii_letters)
listNumbers = list(string.digits)
listSpecialCharacters = list(string.punctuation)

"""
Password to Crack
We recommend just 4 characters or less, 
there can be more, but then it will take longer to find the right combination

Test cases:
      "0a!"
      "aa0@"
      "Aa*1"
      "ab@0"
"""

print("Enter the password that you want to crack")
psw = str(input()) 

"""
In order to access the different positions of the password string,
the string has to be converted to the list 
"""

def createListString(password):
    p = []
    for x in range(len(password)):
        p.insert(x, listLetters[0])
    return p

"""
Loops over all possible characters: Letters, Numbers and Symbols using 'for loop'
"""

def loopListCharacters(password, pos):
    stop = False
    start = 0
    flag = True
    if pos < (len(password)-1):
         start = 1
    for z in range(start,len(listLetters)):
            password[pos] = listLetters[z]
            if pos < (len(password)-1):
                 stop = loopListCharacters(password,pos+1)
                 flag = False
            if stop:
                 break
            if flag:
                p = "".join(password)
                # print(p)
                if p==psw:
                    print(f"Password is: {p}")
                    stop = True
                    break
    if stop:
         return stop
    
    for n in range(len(listNumbers)):
            password[pos] = listNumbers[n]
            if pos < (len(password)-1):
                 stop = loopListCharacters(password,pos+1)
                 flag = False
            if stop:
                 break
            if flag:
                p = "".join(password)
                # print(p)
                if p==psw:
                    print(f"Password is: {p}")
                    stop = True
                    break
    if stop:
         return stop

    for c in range(len(listSpecialCharacters)):
            password[pos] = listSpecialCharacters[c]
            if pos < (len(password)-1):
                 stop = loopListCharacters(password, pos+1)
                 flag = False
            if stop:
                 break
            if flag:
                p = "".join(password)
                # print(p)
                if p==psw:
                    print(f"Password is: {p}")
                    stop = True
                    break
    return stop

"""
-------------- Main Function ----------------------------------
It starts with the last character and tests with all possible options,
then test changing the first character and repeat the process,
keep trying with all possibilities with the first character, 
then starts to change front to back, the next position and repeating the same process
"""

def passwordCracker(password):
    stop = False
    for y in reversed(range(1, len(password))):
        for x in range(len(listLetters)):
            password[0] = listLetters[x]
            stop = loopListCharacters(password, y)
            if stop:
                break
        if stop:
                break
        for w in range(len(listNumbers)):
            password[0] = listNumbers[w]
            stop = loopListCharacters(password, y)
            if stop:
                break
        if stop:
                break
        for z in range(len(listSpecialCharacters)):
            password[0] = listSpecialCharacters[z]
            stop = loopListCharacters(password, y)
            if stop:
                break
        if stop:
                break
            
passwordCracker(createListString(psw))             
    