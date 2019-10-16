# this code will accept an input string and check if it is a plandrome
# it will then return true if it is a plaindrome and false if it is not


def reverse(str1):
    if(len(str1) == 0):
        return str1
    else:
        return reverse(str1[1:]) + str1[0]


string = input("Please enter your own String : ")

# check for strings
str1 = reverse(string)
print("String in reverse Order :  ", str1)

if(string == str1):
    print("This is a Palindrome String")
else:
    print("This is Not a Palindrome String")
