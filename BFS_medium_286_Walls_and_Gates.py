class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.

        BFS
        """
        if not rooms:    return   # 特判
        
        m, n = len(rooms), len(rooms[0])
        visit = [[0]*n for _ in range(m)]
        queue = []  # 队列
        for i in range(m):
            for j in range(n):
                if not rooms[i][j]:  # 为0
                    queue.append([i, j])
                    visit[i][j] = 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            row, col = queue.pop(0)
            for a, b in directions:
                if 0 <= row+a < m and 0 <= col+b < n and rooms[row+a][col+b] != -1 and not visit[row+a][col+b]:
                    # rooms[row+a][col+b] = min(rooms[row+a][col+b], rooms[row][col] + 1)
                    rooms[row+a][col+b] = rooms[row][col] + 1
                    visit[row+a][col+b] = 1
                    queue.append([row+a, col+b])
