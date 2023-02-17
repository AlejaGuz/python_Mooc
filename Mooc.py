import string

password = ""

"""
All functions using the recursivity, it's mean that they call themselfs

The algorithm starts back to front with the last character position, 
it tests with all possibles characters, if it doesn't equals to the password,
changes the previous position character and repeat the proccess until it find the given password 

@pos : the currently position of character in the string of testing password
@cant : length of password
@passwd: the string that makes the changes so we can pass again when the the function calls itself
and compare with the given password
"""
def loopLetters (pos, cant, passwd):
    stop = False 

    start = 0

    if pos == 0:
        start = 1        
    
    for x in range(start,len(listLetters)):
        p = passwd+listLetters[x]

        if (cant - pos) == 0:
            print(p)
            if(p == password):
                print(f"el password es: {p}")
                stop = True
                break
        else:
            stop = loopLetters(pos+1,cant,p)
            if not stop:
                stop = loopNumbers(pos+1,cant,p)
    
            if not stop:
                stop = loopSpecialChar(pos+1,cant,p)
        if stop:
            break

    global lastPass 
    lastPass = p
    return stop

def loopSpecialChar (pos, cant, passwd):
    stop = False

    for x in range(0,len(listSpecialCharacters)):
        p = passwd+listSpecialCharacters[x]

        if (cant - pos) == 0:
            print(p)
            if(p == password):
                print(f"el password es: {p}")
                stop = True
                break
        else:
            stop = loopSpecialChar(pos+1,cant,p)
            
            if not stop:
                stop = loopLetters(pos+1,cant,p)
            
            if not stop:
                stop = loopNumbers(pos+1,cant,p)
    
        if stop:
            break

    global lastPass 
    lastPass = p
    return stop

def loopNumbers (pos, cant, passwd):
    stop = False

    for x in range(0,len(listNumbers)):
        p = passwd+listNumbers[x]

        if (cant - pos) == 0:
            print(p)
            if(p == password):
                print(f"el password es: {p}")
                stop = True
                break
        else:
            stop = loopNumbers(pos+1,cant,p)

            if not stop:
                stop = loopLetters(pos+1,cant,p)
            
            if not stop:
                stop = loopSpecialChar(pos+1,cant,p)
    
        if stop:
            break

    global lastPass 
    lastPass = p
    return stop


"""
Challenge: to create a password cracker using Brute Force Technique
Our approach is first to loop over the letters, then over digits and finally over special characters.
"""

def passwordCracker (psw):
    
    global password 
    password = psw

    pss = ""

    cant = len(password)

    for x in range(0,cant-1):
        pss += listLetters[0]

    stop = False

    for x in reversed(range(cant)):

        stop = loopLetters(x,cant-1,pss[:x])

        #print(lastPass)

        if stop:
            break

        stop = loopNumbers(x,cant-1,pss[:x])

        #print(lastPass)

        if stop:
            break

        stop = loopSpecialChar(x,cant-1,pss[:x])

        #print(lastPass)

        if stop:
            break
        

listLetters = list(string.ascii_letters)
listNumbers = list(string.digits)
listSpecialCharacters = list(string.punctuation)

#lastPass = ""
passwordCracker("PasS123!")

