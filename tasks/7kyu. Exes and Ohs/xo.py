# name: Exes and Ohs
# url: https://www.codewars.com/kata/55908aad6620c066bc00002a
# Check to see if a string has the same amount of 'x's and 'o's. The method
# must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
    lowerStr = s.lower()
    return lowerStr.count('o') == lowerStr.count('x')


if __name__ == '__main__':
    print(xo("ooxx")) # => true
    print(xo("xooxx")) # => false
    print(xo("ooxXm")) # => true
    print(xo("zpzpzpp")) # => true // when no 'x' and 'o' is present should return true
    print(xo("zzoo")) # => false