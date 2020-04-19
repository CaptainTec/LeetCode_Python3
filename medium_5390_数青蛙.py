def minNumberOfFrogs(croakOfFrogs):
    import collections
    key_dict = collections.Counter(croakOfFrogs)
    if len(set(key_dict.values())) > 1:
        return -1
    res = 0
    mid = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    complete = 0
    for ele in croakOfFrogs:
        mid[ele] += 1
        if mid['c'] >= mid['r'] >= mid['o'] >= mid['a'] >= mid['k']:
            key = True
            for v in mid.values():
                if v - complete == 0:
                    key = False
                    break
            if key:  # 全非0
                res = max(res, max(list(mid.values()))-complete)
                complete += 1
        else:
            return -1
    return res    

ss = "crcoackkroakroa"
res = minNumberOfFrogs(ss)
print(res)