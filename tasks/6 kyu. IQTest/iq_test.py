# name: IQ Test
# url: https://www.codewars.com/kata/552c028c030765286c00007d
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one
# of the given numbers differs from the others. Bob observed that one number usually differs
# from the others in evenness. Help Bob — to check his answers, he needs a program that among
# the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the
# elements start from 1 (not 0)
def iq_test(numbers):
    evenIndex, oddIndex = -1, -1
    countEven, countOdd = 0, 0
    for i, n in enumerate(numbers.split(" ")):
        if int(n) % 2 == 0:
            if countEven == 0:
                evenIndex = i
            countEven = countEven + 1
        else:
            if countOdd == 0:
                oddIndex = i
            countOdd = countOdd + 1

        if countOdd > 1 and evenIndex != -1:
            return evenIndex + 1
        if countEven > 1 and oddIndex != -1:
            return oddIndex + 1
    return 0

# Others solutions 1
def iq_test_good1(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1

# Others solutions 2
def iq_test_good2(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1

if __name__ == '__main__':
    print(iq_test("2 4 7 8 10"))