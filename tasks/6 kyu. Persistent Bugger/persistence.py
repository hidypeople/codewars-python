# name: Persistent Bugger
# url: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Write a function, persistence, that takes in a positive parameter num and returns its
# multiplicative persistence, which is the number of times you must multiply the digits
# in num until you reach a single digit.
def persistence(n):
    if n < 10:
        return 0
    return persistence_recursive(n, 0)

def persistence_recursive(n, depth):
    curr = n
    result = 1
    while curr >= 10:
        result *= curr%10
        curr = curr // 10
    result *= curr
    if result >= 10:
        return persistence_recursive(result, depth+1)
    return depth+1


if __name__ == "__main__":
    print(persistence(25))