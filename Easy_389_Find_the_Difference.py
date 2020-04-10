def findTheDifference(s, t):
    mid_dict = {}
    for one in s:
        if one in mid_dict:
            mid_dict[one] += 1
        else:
            mid_dict[one] = 1
    print(mid_dict)
    for one in t:
        if one in mid_dict:
            mid_dict[one] -= 1
            if mid_dict[one] == 0:
                del mid_dict[one]
        else:
            return one


s = 'abc'
t = 'abcd'
# res = findTheDifference(s, t)
# print(res)

a = [1, 2, 3, 10, 11]
b = [str(_) for _ in a]
print(sorted(b))
