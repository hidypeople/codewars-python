# name: Find the odd int
# url: https://www.codewars.com/kata/54da5a58ea159efa38000836
# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    result = {}
    for i in seq:
        if result.get(i) == None:
            result[i] = 1
        else:
            result[i] = result[i]+1
    for key in result.keys():
        if result[key] % 2 == 1:
            return key
    return None

# Others solutions 1
def find_it_good1(seq):
    result = 0
    for x in seq:
        result ^= x
    return result

# Other solutions 2
def find_it_good2(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

if __name__ == '__main__':
    print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))