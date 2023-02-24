import string

password = ""

"""
Challenge: to create a password cracker using Brute Force Technique
Our approach is first to loop over the letters, then over digits and finally over special characters.

All functions are recursive, which means that they call themselves.

The algorithm goes from back to front starting with the last character position.
It tests with all possible characters, and if a character doesn't equal the one in the password, then
the previous position character changes and the process repeats until the given password is found.   

@passwd: the string that makes the changes so we can pass again when the the function calls itself
and compare with the given password
"""

def loopLetters(current_position, password_length, passwd):
    stop = False
    start = 0
    if current_position == 0:
        start = 1        
    
    for x in range(start, len(listLetters)):
        p = passwd+listLetters[x]
        if (password_length - current_position) == 0:
            print(p)
            if(p == password):
                print(f"the password is: {p}")
                stop = True
                break
        else:
            stop = loopLetters(current_position+1, password_length, p)
            if not stop:
                stop = loopNumbers(current_position+1, password_length, p)
    
            if not stop:
                stop = loopSpecialChar(current_position+1, password_length, p)
        if stop:
            break
    global lastPass 
    lastPass = p
    return stop

def loopSpecialChar(current_position, password_length, passwd):
    stop = False
    start = 0
    if current_position == 0:
        start = 1

    for x in range(start,len(listSpecialCharacters)):
        p = passwd+listSpecialCharacters[x]
        if (password_length - current_position) == 0:
            print(p)
            if(p == password):
                print(f"the password is: {p}")
                stop = True
                break
        else:
            stop = loopSpecialChar(current_position+1, password_length, p)
            if not stop:
                stop = loopLetters(current_position+1, password_length, p)
            if not stop:
                stop = loopNumbers(current_position+1, password_length, p)
        if stop:
            break

    global lastPass 
    lastPass = p
    return stop

def loopNumbers(current_position, password_length, passwd):
    stop = False
    start = 0
    if current_position == 0:
        start = 1

    for x in range(start,len(listNumbers)):
        p = passwd+listNumbers[x]
        if (password_length - current_position) == 0:
            print(p)
            if(p == password):
                print(f"the password is: {p}")
                stop = True
                break
        else:
            stop = loopNumbers(current_position+1, password_length, p)
            if not stop:
                stop = loopLetters(current_position+1, password_length, p)
            if not stop:
                stop = loopSpecialChar(current_position+1, password_length, p)
        if stop:
            break

    global lastPass 
    lastPass = p
    return stop

def passwordCracker(psw):
    global password 
    password = psw
    pss = ""
    password_length = len(password)

    for x in range(0,password_length-1):
        pss += listNumbers[0]

    stop = False

    for x in reversed(range(password_length)):
        stop = loopNumbers(x,password_length-1,pss[:x])
        #print(lastPass)
        if stop:
            break
        stop = loopSpecialChar(x,password_length-1,pss[:x])
        #print(lastPass)
        if stop:
            break
        stop = loopLetters(x,password_length-1,pss[:x])
        #print(lastPass)
        if stop:
            break

listLetters = list(string.ascii_letters)
listNumbers = list(string.digits)
listSpecialCharacters = list(string.punctuation)

#lastPass = ""
passwordCracker("bA@0")

