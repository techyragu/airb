
def colorful(A):
    digits = []
    digits = []
    while A > 0:
        digit = A%10
        digits.append(digit)
        A //= 10

    digits = digits[::-1]
    print(digits)
    hashset = set(digits)
    for i in range(len(digits)):
        p = digits[i]
        for j in range(1, len(digits)):
            print(i, j)
            print(hashset)
            p = p * digits[j]
            if p in hashset:
                return 0
            hashset.add(p)

    return 1

#print(colorful(239))

def largestNumber(A):
    return "".join(sorted(A, cmp = lambda x, y: int(str(x)+str(y)) -  int(str(y)+str(x))))

largestNumber([1, 4, 50,30])

