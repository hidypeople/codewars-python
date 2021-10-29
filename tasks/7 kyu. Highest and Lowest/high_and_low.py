# name: Highest and Lowest
# url: https://www.codewars.com/kata/554b4ac871d6813a03000035
# In this little assignment you are given a string of space separated numbers, 
# and have to return the highest and lowest number.
# Notes
#   All numbers are valid Int32, no need to validate them.
#   There will always be at least one number in the input string.
#   Output string must be two numbers separated by a single space, and highest number is first.
def high_and_low(numbers):
    min = float('inf')
    max = float('-inf')
    for n in map(int, numbers.split(' ')):
        if min > n:
            min = n
        if max < n:
            max = n
    return ' '.join([str(max), str(min)])

if __name__ == '__main__':
    print(high_and_low("1 2 3 4 5"))  # return "5 1"
    print(high_and_low("1 2 -3 4 5")) # return "5 -3"
    print(high_and_low("1 9 3 4 -5")) # return "9 -5"