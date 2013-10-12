def checkio(text):
    text=text.lower()
    d={i: text.count(i) for i in text if i.isalpha()}
    return max(sorted(d.keys()),key=lambda k:d[k])
    
    

    #replace this for solution
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
