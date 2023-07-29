def rangeSum(A, B):
    # create an in place prefix array
    for i in range(1, len(A)):
        print(i)
        pf[i] = pf[i-1] + A[i]

    # iterate query array
    ans = []
    for l, r in B:
        if l == 0:
            ans.append(pf[r])
        else:
            ans.append(pf[r] - pf[l-1])

    return ans

A = [7, 3, 1, 5, 5, 5, 1, 2, 4, 5]
B = [
  [6, 9],
  [2, 9],
  [2, 4],
  [0, 9]
]
print(rangeSum(A,B))