from collections import deque

def bfs(graph,start_node,visited):
    queue = deque()
    #시작 노드 큐 넣기
    queue.append(start_node)
    #방문처리
    visited[start_node] = True

    while queue:
        #큐 빼기
        v = queue.popleft()
        print(v,end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

bfs(graph,1,visited)