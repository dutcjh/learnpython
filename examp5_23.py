# -*- coding: utf-8 -*-
"""
汉诺塔问题
"""

def printMove(x,y):
    print('move from '+str(x)+' to '+str(y))
    
def Towers(n,one,two,three):
    if n==1:
        printMove(one,three)
    else:
        Towers(n-1, one, three, two)
        printMove(one, three)
        Towers(n-1, two, one, three)
        
Towers(5,'A','B','C') 
#print(Towers(3,'A','B','C'))