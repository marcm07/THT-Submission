# import numpy as np
import unittest

# isbn10 verfication multiply each digit with the corresponding number in the multiplyArray
def isbn10(num):
    multiplyArray = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sum = 0
    for i in range(10):
        if i == 9:
            if num[i] == 'X':
                #subsititue X with 10
                sum = sum + 10*multiplyArray[i]
            else: 
                sum = sum + int(num[i])*multiplyArray[i]        
        else: 
            sum = sum + int(num[i])*multiplyArray[i]
    return sum
    
#isbn13 verfication multiply each digit with the corresponding number in the multiplyArray
def isbn13(num):
    multiplyArray = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
    sum = 0
    for i in range(13):
        sum = sum + int(num[i])*multiplyArray[i]
    return sum

#Converts a valid Isbn10 book to Isbn13
def convertToIsbn13(num):
    removeLastDigit = '978' + num[:-1]
    for i in range(10):
        isbn13Num = removeLastDigit + str(i)
        if isbn13(isbn13Num)%10 == 0:
            return isbn13Num


#function checks whether a Books ISBN is valid for either isbn10 or isbn 13
def checkBookIsbn(bookNum):
    numLength = len(bookNum)
    if numLength == 13: #isbn13
        if isbn13(bookNum)%10 == 0:
            return "Valid"
        else:
            return "Invalid"
    elif numLength == 10: #isbn10
        if isbn10(bookNum)%11 == 0:
            #valid isbn10 -> convert to isbn13
            return convertToIsbn13(bookNum)
        else:
            return "Invalid"
    else: #incorrect length for both isbn10 or isbn13
        return "Invalid"


class TestStringMethods(unittest.TestCase):
# test function to test valid and invalid isbnnumbers
    def test_valid_isbn13numbers(self):
        self.assertEqual(checkBookIsbn('9780316066525'),'Valid')
        self.assertEqual(checkBookIsbn('9783866155237'),'Valid')
        self.assertEqual(checkBookIsbn('9780345453747'),'Valid')

    def test_invalid_isbnnumbers(self):
        self.assertEqual(checkBookIsbn('031606652X'),'Invalid')
        self.assertEqual(checkBookIsbn('9783876155237'),'Invalid')
        self.assertEqual(checkBookIsbn('0345453747'),'Invalid')
        self.assertEqual(checkBookIsbn('123456'),'Invalid')
        self.assertEqual(checkBookIsbn('123456789012345678'),'Invalid')

    def test_valid_isbn10numbers(self):
        self.assertEqual(checkBookIsbn('0316066524'),'9780316066525')
        self.assertEqual(checkBookIsbn('3866155239'),'9783866155237')
        self.assertEqual(checkBookIsbn('817450494X'),'9788174504944')


if __name__ == '__main__':
    unittest.main()

