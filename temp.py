def lesser_of_two_evens(a,b):
    if a%2 is 0 and b%2 is 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a < b:
            return b
        else:
            return a

print(lesser_of_two_evens(99,10))
#################################
def animalCrackers(s1, s2):
    if s1[0] == s2[0]:
        print('True')
        return True
    else:
        print('False')
        return False

animalCrackers('[ello', '[i')
#################################
def makesTwenty(a,b):
    if a is 20 or b is 20:
        return True
    elif a+b is 20:
        return True
    else:
        return False

print(makesTwenty(2,3))
#################################
def oldMacdonald(s):
    s1 = s[0:3].capitalize()
    s2 = s[3:].capitalize()
    return s1+s2
print(oldMacdonald('macdonald'))
#################################
def masterYoda(s):
    word = []
    i = 0
    s = list(s)
    while s[i] == " ":
        word.append(s[i])
        i += 1
    return word
print(masterYoda('Hello There'))
#################################
def almostThere(n):
    if abs(100-n) <= 10 or abs(200-n) <= 10:
        return True
    else:
        return False
print(almostThere(100))
#################################
def has33(n):
    s = list(enumerate(n))
    for k,v in s:
        if (v) == 3:
            return True
        else:
            return False
print(has33([3,3,3]))
#################################
def paperDoll(s):
    word = str()
    for x in s:
        word = word + (x*3)
    print(word)
paperDoll('Pranav')
#################################
def blackJack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    else:
        if a is 11 or b is 11 or c is 11:
            return a+b+c-10
        else:
            return 'BUST'
print(blackJack(9,9,9))
#################################
def summer69(n):
    sum = 0
    for x in n:
        if x is 6:
            n.remove(x)
            
    for x1 in n:
        sum += x1
    return sum
print(summer69([4, 5, 6, 7, 8, 9]))
