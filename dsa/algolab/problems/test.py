
def combine(A, B):
    ans = []
    solve(1, A+1, B, ans, [])
    return ans


def solve(start, end, count, ans, pair):
    if len(pair) == count:
        ans.append(pair[:])

    for i in range(start, end):
        pair.append(i)
        solve(i+1, end, count, ans, pair)
        pair.pop()

print(combine(10,2))