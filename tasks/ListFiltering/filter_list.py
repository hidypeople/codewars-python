# name: List Filtering
# url: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# In this kata you will create a function that takes a list of non-negative integers 
# and strings and returns a new list with the strings filtered out.
def filter_list(l):
    return list(filter(lambda x: type(x) is int, l))

if __name__ == "__main__":
    print(filter_list([1,2,'a','b']))