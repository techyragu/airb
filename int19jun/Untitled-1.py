"""
---
Input :
List a = [3,1,2,5,4]
List b = [8,4,5,7,6]

Output :
[3, 1, 2, 8, 7, 6]

---

Input :
List a = ["chemistry", "maths", "physics", "english", "hindi"]
List b = ["english", "economics", "hindi", "statistics", "probability"]

Output :
["chemistry", "maths", "physics", "economics", "statistics", "probability"]
"""

def remove_common(l1, l2):
    l1_dict = {k: 1 for k in l1}
    l2_dict = {k:1 for k in l2}
    out = []

    for ele in l1:
        if ele in l2_dict:
            continue
        out.append(ele)

    for ele in l2:
        if ele in l1_dict:
            continue
        out.append(ele)

    return out

a = [3,1,2,5,4]
b = [8,4,5,7,6]
print(remove_common(a,b))

    



