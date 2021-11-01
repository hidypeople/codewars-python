# name: Are they the "same"?
# url: https://www.codewars.com/kata/550498447451fbbd7600041c
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks 
# whether the two arrays have the "same" elements, with the same multiplicities. "Same" 
# means, here, that the elements in b are the elements in a squared, regardless of the order.
def comp(a1, a2):
    return None not in (a1, a2) and sorted(i**2 for i in a1) == sorted(a2)

if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2), True)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2), False)
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    print(comp(a1, a2), False)