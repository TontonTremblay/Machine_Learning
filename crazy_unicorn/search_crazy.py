import copy
from collections import deque
import sys

sys.setrecursionlimit(12000)

def RotateOnce(s):
    #Expecting the whole square with its ID. 
    #rotate the square, e.g. push everyone to the right
    sp = deque(copy.deepcopy(s[1]))
    sp.rotate(1)
    return [s[0],list(sp)]


def checkBoard(a):
    #Board is stored in a. 
    #012
    #345
    #678

    #Check center
    direction = ('n','w','e','s')
    s1 = a[4]
    s2p = [1,3,5,7]

    for i in range(len(direction)):
        if a[s2p[i]] is None or s1 is None:
            continue
        if checkCouple(s1,a[s2p[i]], direction[i]) is False:
            return False
    
    #Check 1 and 7
    direction = ['w','e']
    s1 = a[1]
    s2p = [0,2]

    for i in range(len(direction)):
        if a[s2p[i]] is None or s1 is None:
            continue
        if checkCouple(s1,a[s2p[i]], direction[i]) is False:
            return False
    
    s1 = a[7]
    s2p = [6,8]

    for i in range(len(direction)):
        if a[s2p[i]] is None or s1 is None:
            continue
        if checkCouple(s1,a[s2p[i]], direction[i]) is False:
            return False

    #Check 3 5
    direction = ['n','s']

    s1 = a[3]
    s2p = [0,6]

    for i in range(len(direction)):
        if a[s2p[i]] is None or s1 is None:
            continue
        if checkCouple(s1,a[s2p[i]], direction[i]) is False:
            return False

    s1 = a[5]
    s2p = [2,8]


    for i in range(len(direction)):
        if a[s2p[i]] is None or s1 is None:
            continue
        if checkCouple(s1,a[s2p[i]], direction[i]) is False:
            return False

    return True

def checkCouple(s1,s2,direction):
    #the direction tells me how s2 is located from the perspective 
    #of s1. 
    # For example in the following direction is 'n' or 
    #  s2
    #  s1
    #
    # print direction
    # print s1
    # print s2

    if direction is 'n':
        if  s1[1][1][0] is s2[1][3][0] and \
            not s1[1][1][1] is s2[1][3][1]:
            return True
    elif direction is 's':
        if  s1[1][3][0] is s2[1][1][0] and \
            not s1[1][3][1] is s2[1][1][1]:
            return True 
    elif direction is 'w':
        if  s1[1][0][0] is s2[1][2][0] and \
            not s1[1][0][1] is s2[1][2][1]:
            return True 
    elif direction is 'e':
        if  s1[1][2][0] is s2[1][0][0] and \
            not s1[1][2][1] is s2[1][0][1]:
            return True         

    return False
def printFace(card):
    d = {0:'W',1:'N',2:'E',3:'S'}
    c = {0:'red',1:'yel',2:'gre',3:'pin'}
    f = {0:'a',1:'f'}

    print card[0],'[',
    j = 0
    for i in card[1]:

        print d[j],":",c[i[0]],f[i[1]], ",",
        j+=1
    print ']'
def printSolution(a):
    d = {0:'W',1:'N',2:'E',3:'S'}
    c = {0:'red',1:'yel',2:'gre',3:'pin'}
    f = {0:'a',1:'f'}
    # r = 0, y = 1, g = 2, p 
    print '\n',"---"
    for i in range(len(a)):
        if not i is 0 and i % 3 is 0:
            print
        if a[i] is None:
            print "0 Col F",",",
        else:
            #print north direction colour
            # print a[i][1][1][1]
            print a[i][0],c[a[i][1][1][0]],f[a[i][1][1][1]],",",

    print '\n',"---"
    print a
def printBoard(a):
    # print '\n','---'
    for i in range(len(a)):
        if i % 3 is 0:
            print
        
        if a[i] is None:
            print 0,
        else:
            print a[i][0],
    print '\n',"---"
#Search solution algorithm. 
def SearchSolution(a,cards):
    #a has the board, c the cards, t has the tried so far at pos
    p = -1
    used_card = []
    for i in range(len(a)):
        if a[i] is None:
            p = i
            break
        else:
            used_card.append(a[i][0])
    #want to find a good candidate for p. 
    #pick the first card, rotate it until it fits. 
    for c in cards:
        if c[0] in used_card:
            continue
        #This card was not used. 
        #Try to make it fit there by trying all combinations. 
        ct = c 
        for i in range(4):
            if not i is 0:
                ct = RotateOnce(ct)
            at = copy.deepcopy(a)
            at[p] = ct
            if checkBoard(a):
                # print "found"
                # print a[0]
                # print a[1]
                SearchSolution(at,cards)
            else:
                global sol_num 
                sol_num +=1
                
    # if p is -1 and checkBoard(a):
        # print "sol"
        # printSolution(a)
        # for i in a:
            # printFace(i)
        # quit()

# Direction position array: W,N,E,S
# Colour, r = 0, y = 1, g = 2, p = 3
# ass = 0, front = 1
# first is colour, piece
# ass as to front with colour
c = [[1,[(1,0),(3,1),(2,1),(0,0)]],
     [2,[(2,0),(0,1),(1,1),(3,0)]],
     [3,[(0,1),(2,1),(0,0),(3,0)]],
     [4,[(3,0),(1,0),(0,1),(1,1)]],
     [5,[(0,0),(2,0),(3,1),(1,1)]],
     [6,[(2,1),(0,0),(2,0),(3,1)]],
     [7,[(0,0),(1,1),(2,1),(3,0)]],
     [8,[(3,0),(1,1),(2,1),(1,0)]],
     [9,[(1,1),(1,0),(3,0),(2,1)]]]

sol_num = 0 
a = [None for i in range(9)]
# a[0] = c[0]
# printFace(a[0])
# printSolution(a)
# a = eval("[[1, [(2, 1), (0, 0), (1, 0), (3, 1)]], [5, [(1, 1), (0, 0), (2, 0), (3, 1)]], [3, [(2, 1), (0, 0), (3, 0), (0, 1)]], [9, [(1, 0), (3, 0), (2, 1), (1, 1)]], [8, [(1, 0), (3, 0), (1, 1), (2, 1)]], [7, [(3, 0), (0, 0), (1, 1), (2, 1)]], [4, [(3, 0), (1, 0), (0, 1), (1, 1)]], [6, [(0, 0), (2, 0), (3, 1), (2, 1)]], [2, [(3, 0), (2, 0), (0, 1), (1, 1)]]]")
# print checkBoard(a)
# print checkCouple(a[4],a[3],'w')
# print checkCouple(a[3],a[4],'e')
SearchSolution(a,c)
print sol_num