one=['','I','II','III','IV','V','VI','VII','VIII','IX']
ten=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
hun=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
tou=['','M','MM','MMM']
def checkio(data):
    roman=''
    if 1<=data<10:
        return one[data]
    elif data<100:
        roman=ten[int(data/10)]
        if data%10:
            roman+=checkio(data%10)
        return roman
    elif data<1000:
        roman=hun[int(data/100)]
        if data%100:
            roman+=checkio(data%100)
        return roman
    elif data<4000:
        roman=tou[int(data/1000)]
        if data%1000:
            roman+=checkio(data%1000)
        return roman
    else:
        return 'invalid'
    

    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'