#Your optional code here
#You can import some modules or create additional functions


def checkio(line):
    #Your code here
    #It's main function. Don't remove this function
    #It's using for auto-testing and must return a result for check.  
    newlist=[]
    newstr=line.split('-')
    for i in newstr:
        if i.isalpha():
            newlist.append(i)
        elif i.isdigit():
            newlist.append(i)
    #replace this for solution
    return "-".join(newlist)

#Some hints
#you can use split and join methods from string.
#If you used replace() -- don't forget about three or four dashes
#Maybe regexp

#These "asserts" using only for self-checking and not necessary for auto-testing    
if __name__ == '__main__':
    assert checkio('I---like--python') == "I-like-python", 'Example'
