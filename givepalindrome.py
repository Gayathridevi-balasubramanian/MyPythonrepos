def ispalindrome(str):
    return str == str[::-1]

b = ispalindrome('madam')
if b == True:
    print ("It is a palindrome!!")
else:
    print("It is not a palindrome")


    