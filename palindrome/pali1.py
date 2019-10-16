# writing a check if a number is a plaindrome in a quick and easy way

string = input("Please enter a string to check : ")


def palindrome():
    if string == string[:: -1]:
        return True
    else:
        return False


string = palindrome()
if string == True:
    print("This is a palindrome string")
else:
    print('This is not a palindrome')
