""" A fibonnaci is a series of numbers 
where each member is formed from the sum of the last two numbers """


def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
