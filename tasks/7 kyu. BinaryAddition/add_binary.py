# name: Binary Addition
# url: https://www.codewars.com/kata/551f37452ff852b7bd000139
# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string
def add_binary(a,b):
    mult = a + b
    result = ""
    while mult > 0:
        result = ("1" if mult % 2 > 0 else "0") + result
        mult //= 2
    return result

if __name__ == '__main__':
    print(add_binary(5, 9))