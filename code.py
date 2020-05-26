# --------------
import sys

def palindrome(num):
    for i in range(num + 1, sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
            break;

    return res

palindrome(1331)


# --------------
#Code starts here

def a_scramble(str_1, str_2):
    curStr = str_1.lower().replace(" ", "")
    
    for i in range(0, len(str_2)):
        exists = str_2[i].lower() in curStr
        
        if (exists == False):
            break
        else:
            curStr = curStr.replace(str_2[i].lower(), '', 1)

    return exists

#a_scramble("Tom Marvolo Riddle", "Voldemort")
#a_scramble("ticket", "chat")
a_scramble("baby shower", "shows")


# --------------
#Code starts here

def check_fib(num):
    res = False
    lst = []
    
    if(num == 0 | num == 1):
        res = True
    else:
        lst.append(0)
        lst.append(1)
        i = len(lst)
        
        while i <= num:
            lst.append(lst[i - 2] + lst[i - 1])
            i = len(lst)
            
            if (lst[-1] == num):
                res = True
                print(lst)
                break
    
    return res

check_fib(376)


# --------------
#Code starts here
def compress(word):
    word = word.lower()
    res = ""
    preChar = ""
    curChar = ""
    charOcc = 0
    
    for i in range(0, len(word)):
        charOcc = 1
        
        if(i > 0):
            preChar = word[i - 1]
        
        curChar = word[i]
        
        for j in range(i + 1, len(word)):
            if (curChar == word[j]):
                charOcc += 1
            else:
                break
                
        if (curChar != preChar):
            res = res + curChar + str(charOcc)
    
    return res

compress("xxcccdex")


# --------------
#Code starts here

def k_distinct(string, k):
    return k == len(list(set(string.lower())))

k_distinct('Messoptamia', 8)
k_distinct('banana', 4)


