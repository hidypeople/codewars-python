# name: Square Every Digit
# url: https://www.codewars.com/kata/546e2562b03326a88e000020
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them. 
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
def square_digits(num):
    x = num
    res = 0
    d = 1
    while x > 0:
        number = x%10
        x = x // 10
        mult = number**2
        if mult > 10:
            res = res + mult * d
            d *= 100
        else:
            res = res + mult * d
            d *= 10
    return res

if __name__ == '__main__':
    print(square_digits(1234))