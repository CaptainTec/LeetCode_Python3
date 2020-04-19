class Solution:
    def getTriggerTime(self, increase, requirements):
        res = [-1] * len(requirements)
        person = [[0, 0, 0]]
        for i in range(len(requirements)):
            if requirements[i][0] == 0 and requirements[i][1] == 0 and requirements[i][2] == 0:
                res[i] = 0
        
        a, b, c = 0, 0, 0
        for j in range(len(increase)):
            a = person[-1][0] + increase[j][0]
            b = person[-1][1] + increase[j][1]
            c = person[-1][2] + increase[j][2]
            person.append([a, b, c])
        
        # print(person)
        
        for i in range(len(requirements)):
            if res[i] < 0:
                left, right = 1, len(person)-1
                while left <= right:
                    mid = (left + right) // 2
                    key = True
                    for index in [0, 1, 2]:
                        if person[mid][index] < requirements[i][index]:
                            key = False
                            break
                    if not key:
                        left = mid + 1
                    else:
                        k = False
                        if person[mid-1][0] < requirements[i][0] or person[mid-1][1] < requirements[i][1] or person[mid-1][2] < requirements[i][2]:
                            k = True
                        if k:  # True
                            res[i] = mid
                            break
                        else:
                            right = mid - 1
        return res

a = [[2,8,4],[2,5,0],[10,9,8]]
b = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]

a = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]]
b = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
res = Solution().getTriggerTime(a, b)
print(res)

