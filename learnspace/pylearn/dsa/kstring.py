def KUniqueCharacters(string):
    k = int(string[0])
    s = string[1:]
    ans = (0, 0, 0) # len. l, r
    l = 0
    cdict = {}
    for r in range(len(s)):
        cdict[s[r]] = 1 + cdict.get(s[r], 0)

        while len(cdict) > k:
            cdict[s[l]] -= 1
            if cdict[s[l]] == 0:
                del cdict[s[l]]
            l += 1

        if r-l+1 > ans[0]:
            ans = (r-l+1, l, r)

    return s[l:r+1]



if __name__ == "__main__":
    print(KUniqueCharacters("3aabacbebebe"))
    #assert KUniqueCharacters("3aabacbebebe") == "cbebebe", "True"


