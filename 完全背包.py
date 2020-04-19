def solve3(vlist,wlist,totalWeight):
    """完全背包问题"""
    totalLength = len(vlist)
    resArr = [0] * (totalWeight+1)
    for i in range(1, totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j-wlist[i]]+vlist[i])
    print(resArr)
    return resArr[-1]

if __name__ == '__main__':
    v = [60,100,120]
    w = [10,20,30]
    weight = 50
    # n = 3
    result = solve3(v,w,weight)
    print(result)