def test(str1):
    temp=[]
    for x in str1:
        if (x=='0'):
            temp.append('0')
        else:
            temp.pop()
    return not temp

str1 = "01010101"
print("Original sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:",str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))