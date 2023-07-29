from collections import deque
def SeatingStudents(arr):
  total = arr[0]
  occ = arr[1:]

  grid = []
  num = 1
  
  while num <= total:
    col = []
    for i in range(2):
      if num not in occ:
        col.append(True)
      else:
        col.append(False)
      num += 1

    grid.append(col)

  print(grid)
  rows = len(grid)
  cols = 2
  count = 0

  def bfs(r, c):
    nonlocal count
    q = deque([])
    q.append((r,c))
    while q:
      r,c = q.popleft()
      if not grid[r][c]:
        continue
      grid[r][c] = False
      for r_, c_ in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nr, nc = r+r_, c + c_
        if  nr < 0 or nc < 0 or nr >= rows or nc >= cols or not grid[nr][nc]:
          continue
        q.append((nr, nc))
        count += 1



#   ans = 0
#   out = []
#   def dfs(r,c, p):
#     nonlocal ans
#     if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1:
#       return

#     if grid[r][c] in occ:
#       return

#     if p:
#       ans += 1
#       out.append((p, grid[r][c]))

#     p = grid[r][c]
#     grid[r][c] = -1

#     dfs(r, c+1, p)
#     dfs(r, c-1, p)
#     dfs(r+1, c, p)
#     dfs(r-1, c, p)
#     #grid[r][c] = -1

  for r in range(rows):
    for c in range(cols):
      #dfs(r,c, 0)
      if not grid[r][c]:
        continue
      bfs(r,c)
  
  #print(out)
  return count

print(SeatingStudents([6, 4]))
print(SeatingStudents([8, 1, 8]))
