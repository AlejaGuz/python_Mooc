"""
Challenge: to create a password cracker using Brute Force Technique

Our approach is first to loop over the letters, then over digits and finally over special characters.
"""

import string

# password = "Aa@0"

def passwordCracker(password):
    listLetters = list(string.ascii_letters)
    listNumbers = list(string.digits)
    listSpecialCharacters = list(string.punctuation)

    lastPassword = ""


    def loopLetters (pos, cant, passwd):
        stop = False
        start = 0

        if pos == 0:
            start = 1

        for x in range(start, len(listLetters)):
            p = passwd+listLetters[x]

            if (cant - pos) == 0:
                #print(p)
                if(p == password):
                    print(f"The password is: {p}")
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

        global lastPassword
        lastPassword = p
        return stop

    def loopSpecialChar (pos, cant, passwd):
        stop = False

        for x in range(0,len(listSpecialCharacters)):
            p = passwd+listSpecialCharacters[x]

            if (cant - pos) == 0:
                #print(p)
                if(p == password):
                    print(f"The password is: {p}")
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

        global lastPassword
        lastPassword = p
        return stop

    def loopNumbers (pos, cant, passwd):
        stop = False

        for x in range(0,len(listNumbers)):
            p = passwd+listNumbers[x]

            if (cant - pos) == 0:
                #print(p)
                if(p == password):
                    print(f"The password is: {p}")
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

        global lastPassword
        lastPassword = p
        return stop

    pss = ""

    cant = len(password)

    for x in range(0,cant-1):
        pss += listLetters[0]

    stop = False

    for x in reversed(range(cant)):

        stop = loopLetters(x,cant-1,pss[:x])

        print(lastPassword)

        if stop:
            break

        stop = loopNumbers(x,cant-1,pss[:x])

        print(lastPassword)

        if stop:
            break

        stop = loopSpecialChar(x,cant-1,pss[:x])

        print(lastPassword)

        if stop:
            break

print(passwordCracker("MyPass234!"))