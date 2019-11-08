# This file contains a function to reverse word,
# For example, given the word Jonathan,
# Then it shall be reversed to nahtanoJ

def reverseWords(input):

    # split the words in the string separated by space
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    # join the spaced words
    reversed_words  = " ".join(inputWords)

    return reversed_words

if __name__ == "__main__":
    input = "I am really becoming good at this"
    print(reverseWords(input))