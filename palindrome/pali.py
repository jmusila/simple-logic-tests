# checking if a number is a palindrome
# using Big O of n O(n)


def string_is_palindrome(string):
    """
    Complexity:
        O(n) time
        O(n) space
    """
    reversed_string = []
    for i in reversed(range(len(string))):
        reversed_string.append(string[i])
    return string == "".join(reversed_string)


string_input = input("Please enter a palindrome string : ")
string = string_is_palindrome(string_input)
print('Is it True or False : ', string)

if(string == True):
    print('This is a Palindrome string')
else:
    print('This is not a Palindrome string')
