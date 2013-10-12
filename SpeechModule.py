FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    Result=('zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen').split(' ')
    Tens=('none none twenty thirty forty fifty sixty seventy eighty ninety').split(' ')
    if number<20:
        return Result[number]
    elif number<100:
        x=Tens[int(number/10)]
        if number%10:
            x+=' ' + checkio(number%10)
        return x
    elif number<1000:
        x=checkio(int(number/100)) + ' hundred'
        if number%100:
            x+=' ' + checkio(number%100)
        return x
            
    

    

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
