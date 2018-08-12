#! Task from http://codingbat.com:
# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
#
# Examples:
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


def xyz_there(str):
    if len(str) < 3:
        return False
    elif len(str) == 3:
        if str == 'xyz':
            return True
        else:
            return False
    else:
        arry_str = str.split('.x')
        for i in range(len(arry_str)):
            new_str = arry_str[i]
            if len(new_str) == 3:
                if new_str == 'xyz':
                    return True
            elif len(new_str) > 3:
                for j in range(len(new_str) - 2):
                    if new_str[j:j + 3] == 'xyz':
                        return True
        return False


print(xyz_there('abcxyz'))  # → True
print(xyz_there('abc.xyz'))  # → False
print(xyz_there('xyz.abc'))  # → True
print(xyz_there('abcxy'))  # → False
print(xyz_there('xyz'))  # → True
print(xyz_there('xy'))  # → False
print(xyz_there('x'))  # → False
print(xyz_there(''))  # → False
print(xyz_there('abc.xyzxyz'))  # → True
print(xyz_there('abc.xxyz'))  # → True
print(xyz_there('.xyz'))  # → False
print(xyz_there('12.xyz'))  # → False
print(xyz_there('12xyz'))  # → True
print(xyz_there('1.xyz.xyz2.xyz'))  # → False
