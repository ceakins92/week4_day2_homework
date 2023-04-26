# In place algo; because it modifies the original list
def reverse_list(alist):
    left, right = 0, len(alist) - 1
    while left < right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1


# Original List
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_list(alist)
# Modified Original List
print(alist)

'racecar'
'racercar'


def check_palindrome(astring):
    left, right = 0, len(astring) - 1
    while left < right:
        left_letter = astring[left]
        right_letter = astring[right]
        if left_letter != right_letter:
            return False
        left += 1
        right -= 1
    return True


print(check_palindrome('racecar'))
print(check_palindrome('matrix'))
