def dfs(graph,cur_node,visited_list):
    visited_list[cur_node] = True

    print(cur_node,end=' ')

    for i in graph[cur_node]:
        if visited_list[i] == False:
            dfs(graph,i,visited_list)

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

dfs(graph,1,visited)