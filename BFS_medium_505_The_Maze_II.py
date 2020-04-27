class Solution:
    # def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    def shortestDistance(self, maze, start, destination):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]    # 定义上下左右四个方向
        m = len(maze)                               # 获取矩阵大小
        n = len(maze[0])

        queue = [(start[0],start[1])]               # 构造队列，并将起始位置包含其中
                                                    # distance保存从起点到每个点的距离
        distance = [[float('inf')]*n for _ in range(m)]
        distance[start[0]][start[1]] = 0

        while queue:
            i,j = queue.pop(0)                      # 弹出坐标值i,j
                                                    # 如果坐标为终点坐标，返回True，程序结束
            
            for dx,dy in directions:                # 对四个方向进行遍历
                x,y,step =i+dx,j+dy,distance[i][j]
                while 0<=x<m and 0<=y<n and maze[x][y] != 1:                                      
                                                    # 当x,y坐标合法，并且对应值为0或-1时
                    x = x+dx                        # 继续前进，模拟小球的滚动过程
                    y = y+dy                        # 其中0为空地，而-1为之前遍历过的空地
                    step += 1

                x = x - dx
                y = y - dy

                # 注意：这里distance[x][y] 是往小变化的，所以不会出现对于全部为0时，无限循环的情况。
                if distance[x][y] > step:           # 如果起点到该点的距离比当前距离大
                                                    # 更新该距离，并将坐标加入队列
                    maze[x][y] = -1                 # 在maze中标记已经遍历过
                    distance[x][y] = step              
                    queue.append((x,y))             # 并将其坐标添加到队列中
                                                    # 如果遍历所有可能性都无法达到目的地
        for one in distance:
            print(one)
        print('-'*20)
        for one in maze:
            print(one)
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float('inf') else -1
