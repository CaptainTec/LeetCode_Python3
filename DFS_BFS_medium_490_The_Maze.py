"""
在没有碰到墙壁之前，或者边界的时候， 这个球会沿着一个方向一直滚动
"""

# DFS
class Solution:
    # def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    def hasPath(self, maze, start, destination):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]    # 定义上下左右四个方向
        m = len(maze)                               # 获取矩阵大小
        n = len(maze[0])
        maze[start[0]][start[1]] = 2
                                                    # 构造dfs函数，其返回值为bool值
        def dfs(m,n,maze,x,y,directions,destination):
            # maze[x][y] = 2                         # -1表示该点已经过遍历，防止循环
                                                    # 如果坐标为终点坐标，返回True
            if x==destination[0] and y==destination[1]:
                return True
            
            res = False
            i,j = x,y                               # 保存坐标值
            for dx,dy in directions:                # 对四个方向进行遍历
                x,y =i,j
                while 0<=x+dx<m and 0<=y+dy<n and (maze[x+dx][y+dy] == 0 or maze[x+dx][y+dy]==2): 
                # 一直朝一个方向走，直到遇到墙壁停下来                                     
                                                    # 当x,y坐标合法，并且对应值为0或-1时
                    x = x+dx                        # 继续前进，模拟小球的滚动过程
                    y = y+dy                        # 其中0为空地，而-1为之前遍历过的空地

                if maze[x][y]!=2:                  # 如果该点的值不为-1，即未遍历过
                                                    # 进行遍历，并对res和遍历结果取或
                                                    # 有True即为True
                    maze[x][y] = 2
                    res = res or dfs(m, n, maze, x, y, directions, destination)
            
            return res                              # 返回res
        
        res = dfs(m, n, maze, start[0], start[1], directions, destination)
        # for one in maze:
        #     print(one)
        return res


# BFS
class Solution2:
    # def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    def hasPath(self, maze, start, destination):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]    # 定义上下左右四个方向
        m = len(maze)                               # 获取矩阵大小
        n = len(maze[0])

        queue = [(start[0],start[1])]               # 构造队列，并将起始位置包含其中
        maze[start[0]][start[1]] = -1               # -1表示该点已经过遍历，防止循环

        while queue:
            i,j = queue.pop(0)                      # 弹出坐标值i,j
                                                    # 如果坐标为终点坐标，返回True，程序结束
            if i == destination[0] and j == destination[1]:
                return True
            for dx,dy in directions:                # 对四个方向进行遍历
                x,y =i,j
                while 0<=x+dx<m and 0<=y+dy<n and (maze[x+dx][y+dy] == 0 or maze[x+dx][y+dy]==-1):                                      
                                                    # 当x,y坐标合法，并且对应值为0或-1时
                    x = x+dx                        # 继续前进，模拟小球的滚动过程
                    y = y+dy                        # 其中0为空地，而-1为之前遍历过的空地
                if maze[x][y]!=-1:                  # 如果该点的值不为-1，即未遍历过
                    maze[x][y] = -1                 # 置为1
                    queue.append((x,y))             # 并将其坐标添加到队列中
            
                                                    # 如果遍历所有可能性都无法达到目的地
        return False                                # 返回False


maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
s = [0,4]
d = [4,4]
# maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
# s = [0,4]
# d = [3,2]
res = Solution().hasPath(maze, s, d)
print(res)