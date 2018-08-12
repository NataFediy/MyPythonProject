#! Task from http://codingbat.com:
# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).
#
# Examples:
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2


def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0

    # last 2 chars, can be written as str[-2:]
    else:
        new_str = str[len(str)-2:]
        count = 0

    # Check each substring length 2 starting at i
        for i in range(len(str)-2):
            sub = str[i:i+2]
            if sub == new_str:
                count = count + 1

    return count


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxaxxaxxaxx'))
print(last2('xaxaxaxx'))
print(last2('xxxx'))
print(last2('13121312'))
print(last2('11212'))
print(last2('13121311'))
print(last2('1717171'))
print(last2('hi'))
print(last2('h'))
print(last2(''))
