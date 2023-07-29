from collections import deque

def bfs(root):
    if not root:
        return []
    ans = []
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        ans = ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return ans
