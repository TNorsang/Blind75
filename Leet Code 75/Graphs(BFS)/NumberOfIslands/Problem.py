from collections import deque
def number_of_islands(graph):
    island_number = 0
    rows, cols = len(graph), len(graph[0])
    visited = set()
    for row in range(rows):
        for col in range(cols):
            if graph[row][col] == "1" and (row,col) not in visited:
                bfs(row,col,visited,graph)
                island_number += 1
    return island_number
def bfs(i,j,visited,graph):
    queue = deque([(i,j)])
    visited.add((i,j))
    directions = [(-1,0),(1,0),(0,1),(0,-1)]
    while queue:
        r, c = queue.popleft()

        for row,col in directions:
            rr, cc = r + row, c + col
            if 0 <= rr < len(graph) and 0 <= cc < len(graph[0]):
                if graph[rr][cc] == "1" and (rr,cc) not in visited:
                    queue.append((rr,cc))
                    visited.add((rr,cc))
        
                
# Returns 3
island_graph = [['1','1','0','0'],
                ['1','1','1','0'],
                ['1','0','0','1'],
                ['1','1','1','0'],
                ['0','0','0','0'],
                ['1','1','1','0']]

print(number_of_islands(island_graph))
