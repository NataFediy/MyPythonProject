#! Task:
# Please provide full program code (on Python language) of parse_number(num) function
# which returns the dict with following structure:
# {odd:number of odd digits in input value, even:number of even digits og input value}
# or False when wrong input value
# NOTE: Assume that the "zero" digit also belongs to even numbers
# EXAMPLE OF: inputs/otputs when using this function:
# >>> print(parse_number(34567)
# {'odd':3, 'even':2}
# >>> print(parse_number(100))
# {'odd':1, 'even':2}
# >>> print(parse_number('word')
# False


def parse_number(num):
    if not str(num).isdigit():
        return False
    else:
        number_dict = {'odd': 0, 'even': 0}

        for num in str(num):
            if int(num) % 2 != 0:
                number_dict['odd'] = number_dict['odd'] + 1
            else:
                number_dict['even'] = number_dict['even'] + 1

        return number_dict


print(parse_number(34567))
print(parse_number(100))
print(parse_number('word'))
