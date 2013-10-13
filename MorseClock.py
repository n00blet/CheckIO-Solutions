def checkio(data):  
    code =[]  
    for i, d in enumerate(data.split(':')): 
        d=int(d)
        y=''
        f=d/10
        s=d%10
        if i==0:
            y+='{0:02b} '.format(f)
        else:
            y+='{0:03b} '.format(f)
        y+='{0:04b}'.format(s)
        code.append(y)
    code=' : '.join(code)
    return code.replace('0','.').replace('1','-')
        
       

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

