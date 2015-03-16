 

#/**********************************************************************/ 

#/* CSC 280 - HW #8

#/* */ 

#/* modifier: Paul Mattioli

#/* */ 

#/* filename:list_instances.py
#/*
#/* modified from: laptop
#/* 

#/* date last modified: 11/24
#/*
#/* program takes inputs of a list, adds to list, counts the number of instances of each item and and returns list stripped of duplicates
#/* */ 

#/**********************************************************************/ 

''' shoppinglist: asks user for input, and appends to a list. also removes x placeholder'''
def shoppinglist():
    grocerylist = []
    x = 'Grocerylist'
    while x != '':
        grocerylist.append(x)
        x = raw_input("Add item: ")
    grocerylist.remove("Grocerylist")
    return grocerylist
'''
sortshoppinglist: uses the exact bubblesort algorithm just applied to names, returns sorted grocerylist'''
def sortshoppinglist(turnips):
    
    for j in range (len(turnips)):
        for i in range (j+1, len(turnips)):
            if turnips[i] < turnips[j]:
                turnips[i], turnips[j] = turnips[j], turnips[i]
    
    return turnips
''' stripshoppinglist: creates place holder list which tests duplicates. outputs list w/o duplicates'''
def stripshoppinglist(chz):
    placehldr = []
    for i in chz:
        if i not in placehldr:
            placehldr.append(i)
    return placehldr

''' reportshoppinglist: reports both lists; w/ and w/o duplicates'''
def reportshoppinglist(g,h):
    print 'list with duplicates: ' + str(h)
    for e in range(0, len(h)):
        f = h.count(h[e])
        print str(h[e]) + ' instances: ' + str(f)

    print 'list stripped of duplicates: ' + str(g)

''' main function calls all functions by setting them to variables.'''

def main():
    print 'welcome to the list instances beta! '
    sl = shoppinglist()
    srtdsl = sortshoppinglist(sl)
    stripshoppinglist(srtdsl)
    stpdsl = stripshoppinglist(srtdsl)
    rsl = reportshoppinglist(stpdsl, srtdsl)
    print rsl
print main()
    
    



    
    
    
