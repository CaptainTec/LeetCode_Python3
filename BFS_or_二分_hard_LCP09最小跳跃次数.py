# class Solution:
#     def minJump(self, jump):
#         n = len(jump)
#         if len(set(jump)) == 1:
#             return n

#         queue = [(0, jump[0], 0)]  # index, value, step
#         index = 0
#         while queue:
#             top = queue.pop(0)
#             if top[0] + top[1] >= n:
#                 return top[2] + 1
#             queue.append((top[0]+top[1], jump[top[0] + top[1]], top[2]+1))
#             for i in range(index+1, top[0]):
#                 queue.append((i, jump[i], top[2]+1))
#             index = max(index, top[0])

# class Solution:
#     def minJump(self, jump):
#         n = len(jump)
#         dp = [float("inf")] * n
#         dp[0] = 0
#         for one in jump:

# # Answer 1
# import collections
# class Solution:
#     def minJump(self, jump):
#         to_final = []
#         fromdict = collections.defaultdict(lambda:[])
#         visited = {}
        
#         for i, t in enumerate(jump) :
#             if i + t >= len(jump) :
#                 to_final.append(i)
#                 visited[i] = 1
#             else :
#                 fromdict[i+t].append(i)
        
#         print(to_final)
#         print(fromdict)
#         print(visited)

#         if 0 in visited :
#             return 1
        
#         ip = 0
#         while ip < len(to_final) :

#             nowp = to_final[ip]
#             nows = visited[nowp]
#             ip += 1
            
#             for nextt in fromdict[nowp] :
#                 if nextt in visited :
#                     continue
#                 visited[nextt] = nows + 1
#                 to_final.append(nextt)
#             for nextt in range(nowp+1, len(jump)) :
#                 if nextt in visited :
#                     if visited[nextt] <= nows :
#                         break
#                     continue
#                 visited[nextt] = nows + 1
#                 to_final.append(nextt)


#             print('*'*10)
#             print(to_final)
#             print(fromdict)
#             print(visited)

#             if 0 in visited :
#                 return visited[0]
                

# Answer 2
class Solution:
    def minJump(self, jump):
        n = len(jump)
        queue = [(0, 0)]

        def cut(idx):
            left[right[idx]], right[left[idx]] = left[idx], right[idx]
            left[idx] = right[idx] = -2
        
        right = [i+1 for i in range(n)]
        left = [i-1 for i in range(n)]
        print(right)
        print(left)

        cut(0)
        print('='*20)
        print(right)
        print(left)
        while queue:
            cur, step = queue.pop(0)
            if cur + jump[cur] >= n:
                return step+1
            if left[cur+jump[cur]] != -2:
                queue.append((cur+jump[cur], step+1))
                cut(cur+jump[cur])
            if cur:
                p = cur - 1
                while p > 0 and left[p] > -2:
                    q = left[p]
                    queue.append((p, step+1))
                    cut(p)
                    p = q
            print('*'*20)
            print(right)
            print(left)
        

jump = [2, 5, 1, 1, 1]
res = Solution().minJump(jump)
print(res)