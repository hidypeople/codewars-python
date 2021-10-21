# name: String incrementer
# url: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# Your job is to write a function which increments a string, to create a new string. 
#   If the string already ends with a number, the number should be incremented by 1. 
#   If the string does not end with a number. the number 1 should be appended to the new string.
#   Attention: If the number has leading zeros the amount of digits should be considered.
def increment_string(s):
    def isDigit(c):
        return c >= '0' and c <= '9'
    if len(s) == 0 or not isDigit(s[-1]):
        return s + "1"

    numberIdx = len(s)
    for c in reversed(s):
        if isDigit(c):
            numberIdx = numberIdx - 1
        else:
            break
    rest = s[numberIdx:]
    nonZeroIdx = 0
    for c in rest:
        if c != '0':
            break
        nonZeroIdx = nonZeroIdx + 1
    number = rest[nonZeroIdx:] if nonZeroIdx < len(rest) else '0'
    print(number)
    next = str(int(number) + 1).rjust(len(rest), '0')
    return s[:numberIdx] + next

if __name__ == '__main__':
    print("", increment_string(""))
    print("foo", increment_string("foo"))
    print("123", increment_string("123"))
    print("foo000", increment_string("foo000"))
    print("foo44", increment_string("foo44"))
    print("foo044", increment_string("foo044"))
    print("foo0011", increment_string("foo0011"))
    print("foo099", increment_string("foo099"))
    print("foo999", increment_string("foo999"))
    print("xi7E1686454000000000677822", increment_string("xi7E1686454000000000677822"))