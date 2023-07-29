from collections import deque
class Solution:
    def alienOrder(self, words):
        graph = {}
        indegs = [0 for i in range(26)]


        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            
            idx = 0
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    node = ord(word1[j]) - ord("a")
                    ng = ord(word2[j]) - ord("a")
                    
                    if node not in graph:
                        graph[node] = set()
                    graph[node].add(ng)

                    if ng not in graph:
                        graph[ng] = set()

                    indegs[ng] += 1
                    break

        print(graph)
        print(indegs)
        
        queue = deque()
        visited = set()
        for ng, indeg in enumerate(indegs):
            if ng in graph and indeg == 0:
                queue.append(ng)
                visited.add(ng)

        result = ""
        while queue:
            node = queue.popleft()
            result += chr(ord('a') + node)
            for ng in graph[node]:
                indegs[ng] -= 1
                if indegs[ng] == 0 and ng not in visited:
                    queue.append(ng)
                    visited.add(ng)

        if len(result) != len(words):
            return ""

        return result
    
s = Solution()
words = ["wrt","wrf","er","ett","rftt"]
words1 = ["ab","cd", "ef", "cg"]
print(s.alienOrder(words1))