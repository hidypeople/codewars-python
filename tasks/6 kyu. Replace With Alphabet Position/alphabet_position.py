# name: Replace With Alphabet Position
# url: https://www.codewars.com/kata/546f922b54af40e1e90001da
# In this kata you are required to, given a string, replace every letter with its position in the 
# alphabet. If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    return ' '.join(map(lambda c: str(ord(c.lower()) - ord('a') + 1), filter(lambda c: c.isalpha(), text)))

if __name__ == '__main__':
    print(alphabet_position("persistence: [Ok]"))