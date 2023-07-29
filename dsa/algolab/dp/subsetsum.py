from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    #return recur(n-1, k, arr)
    dp = []
    for i in range(n):
        dp.append([-1]*(k+1))

    return memoize(n-1, k, arr, dp)

    

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer

def recur(ind, target, arr):
    if target == 0:
        return True
    if ind == 0:
        if target == arr[0]:
            return True
        else:
            return False

    not_pick = recur(ind-1, target, arr)
    if not_pick:
        return True
    pick = False
    if arr[ind] <= target:
        pick = recur(ind-1, target-arr[ind], arr)

    return not_pick or pick

def memoize(ind, target, arr, dp):
    if target == 0:
        dp[ind][target] = True
        return dp[ind][target]
    if ind == 0:
        if target == arr[0]:
            dp[ind][target] = True
            return dp[ind][target]
        else:
            dp[ind][target] = False
            return dp[ind][target]

    if dp[ind][target] != -1:
        return dp[ind][target]

    not_pick = memoize(ind-1, target, arr, dp)
    if not_pick:
        dp[ind][target] = True
        return dp[ind][target]

    pick = False
    if arr[ind] <= target:
        pick = memoize(ind-1, target-arr[ind], arr, dp)

    dp[ind][target] = not_pick or pick
    return dp[ind][taget]

            


    
    
    

