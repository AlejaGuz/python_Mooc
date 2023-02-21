import string

listLetters = list(string.ascii_letters)
listNumbers = list(string.digits)
listSpecialCharacters = list(string.punctuation)

# Password to Crack
# We recommend just 4 characters or less, 
# can be more, but between more it has, longer it takes
# Testing with:
#       "0a!"
#       "aa0@"
#       "Aa*1"
#       "ab@0"
print("Enter the password that you want to crack")
psw = str(input()) 

# We need to access the different positions of my password string,
# the best way to do it, is converting the string to list 
def createListString (password):
    
    p = []

    for x in range(len(password)):
        p.insert(x,listLetters[0]) 

    return p

# Makes the simple "for loop" of all posible characters: Letters, Numbers and Symbols
def loopListCharacters(password,pos):

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

                print(p)

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

                print(p)

                if p==psw:
                    print(f"Password is: {p}")
                    stop = True
                    break
    
    if stop:
         return stop

    for c in range(len(listSpecialCharacters)):
            password[pos] = listSpecialCharacters[c]

            if pos < (len(password)-1):
                 stop = loopListCharacters(password,pos+1)
                 flag = False

            if stop:
                 break
            
            if flag:

                p = "".join(password)

                print(p)

                if p==psw:
                    print(f"Password is: {p}")
                    stop = True
                    break

    return stop

# -------------- Main Function ----------------------------------
# It starts with the last character and tests with all posible options,
# then test changing the first character and repeat the process,
# keep trying with all posibilities with the first character, 
# then starts to change front to back, the next position and repeating the same process
def passwordCracker (password):
    stop = False

    for y in reversed(range(1,len(password))):
        for x in range(len(listLetters)):
            password[0] = listLetters[x]

            stop = loopListCharacters (password,y)

            if stop:
                break

        if stop:
                break
        
        for w in range(len(listNumbers)):
            password[0] = listNumbers[w]

            stop = loopListCharacters (password,y)

            if stop:
                break

        if stop:
                break
        
        for z in range(len(listSpecialCharacters)):
            password[0] = listSpecialCharacters[z]

            stop = loopListCharacters (password,y)

            if stop:
                break

        if stop:
                break
            
passwordCracker(createListString(psw))             
    