'''
200. Number of Islands
Medium

5856

202

Add to List

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

# Using BFS

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","1","1"],
  ["0","1","0","1","1"],
  ["0","1","0","1","1"]]


def numIslands(grid):
  count = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '1':
        count += 1
        bfs(grid, i ,j)
  print(count)


def bfs(grid, i, j):
  if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 \
  or grid[i][j] == '0':
    return 

  grid[i][j] = '0'
  bfs(grid, i + 1, j)
  bfs(grid, i, j + 1)
  bfs(grid, i - 1, j)
  bfs(grid, i, j - 1)
  return


numIslands(grid)


'''
3
'''
