# This file contains a function to reverse word,
# For example, given the word Jonathan,
# Then it shall be reversed to nahtanoJ

def revrseWords(input):

    # split the words in the string separated by space
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    