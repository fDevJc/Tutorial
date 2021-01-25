from collections import deque
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9

queue = deque()
'''
for node_num,node_graph in enumerate(graph):
    queue.append(node_num)
    visited[node_num] = True
    queue.pop()
    print(node_num , end=' ')
    for i in node_graph:
        if not visited[i]:
            queue.append(i)

'''

for i in range(1,9):
    if not visited[i]:
        queue.append(i)
        visited[i]=True
    for j in graph[i]:
        if not visited[j]:
            queue.append(j)
            visited[j]=True

print(queue)