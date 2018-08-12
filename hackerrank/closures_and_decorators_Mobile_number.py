# The given mobile numbers may have +91, 91 or 0 written before
# the actual 10 digit number.
# Alternatively, there may not be any prefix at all.
#
# Input Format:
# The first line of input contains an integer N,
# the number of mobile phone numbers.
# N lines follow each containing a mobile number.
#
# Output Format:
# Print  mobile numbers on separate lines in the required format.
#
# Sample Input:
# 3
# 07895462130
# 919875641230
# 9195969878
#
# Sample Output:
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230
#
# Concept:
# Like most other programming languages, Python has the concept of closures.
# Extending these closures gives us decorators, which are an invaluable asset.
# You can learn about decorators in 12 easy steps here.
# To solve the above question, make a list of the mobile numbers
# and pass it to a function that sorts the array in ascending order.
# Make a decorator that standardizes the mobile numbers and apply it to
# the function.


def wrapper(f):
    def new_phone_number(l):
        f('+91 {0} {1}'.format(n[-10:-5], n[-5:]) for n in l)

    return new_phone_number


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
