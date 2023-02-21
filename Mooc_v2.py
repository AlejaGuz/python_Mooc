import string

listLetters = list(string.ascii_letters)
listNumbers = list(string.digits)
listSpecialCharacters = list(string.punctuation)

password = []
psw = "Aa@0"


def createListString (psw):
     for x in range(len(psw)):
          password.insert(x,listLetters[0]) 

start = 0
stop = False

createListString(psw)

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
         
            
 