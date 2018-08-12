#! Identify whether the phrase or word palindrome or not
import math


def ispalindrome(word):
    if len(word) == 0:
        return True
    else:
        value = []
        for item in word.lower():
            if item.isalpha():
                value.append(item)
        middle = int(math.floor(len(value) / 2))
        for i in range(middle):
            if not value[i] == value[len(value) - 1 - i]:
                return False
        return True


print(ispalindrome(''))  # true
print(ispalindrome('abcdcba'))  # true
print(ispalindrome('abcd'))  # false
print(ispalindrome('A man a plan a canal Panama'))  # true
