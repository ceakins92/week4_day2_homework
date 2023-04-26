# Write a function that takes an array of integers as input, and returns the sum of all the palindromic numbers in the array. If there are no palindromic numbers in the array, the function should return 0.
# A palindromic number is a number that is the same from a reversed order. For example 122 is not a palindromic number, but 202 is one.
# For example:
number1 = [101, 2, 85, 33, 14014]
number2 = [45, 21, 303, 56]
number3 = [12, 34, 56]


def is_palindrome(arr):
    pdromes = []
    for i in arr:
        if str(i) == str(i)[::-1]:
            pdromes.append(i)
    return sum(pdromes)


print(is_palindrome(number1))
