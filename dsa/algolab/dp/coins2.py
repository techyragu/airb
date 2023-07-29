def change(amount, coins):
    if len(coins) == 0:
        return []
        
    ans = []
    def bt(cs, start, amount, coins):
        nonlocal ans
        if amount == 0:
            ans.append(cs[:])
            return 
        if amount < 0:
            return
        
        for i in range(start, len(coins)):
            cs.append(coins[i])
            bt(cs, i, amount-coins[i], coins)
            cs.pop()
    bt([], 0, amount, coins)
    return ans

print(change(5, [1,2,5]))