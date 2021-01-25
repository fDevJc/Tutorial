import heapq

def start(start_node):
    #첫 시작 노드의 비용은 1
    shortway_array[start_node] = 0
    h = []
    heapq.heappush(h,(0,start_node))
    cnt = 1
    while len(h):
        cnt+=1
        if cnt > 4:
            break
        #힙에서 비용 및 노드번호 추출
        cost , node_num = heapq.heappop(h)

        print("node_num :",node_num , " cost : ",cost," visited_array[node_num] : ",visited_array[node_num])

        #방문 체크
        if visited_array[node_num] == True:
            continue
        else: visited_array[node_num] = True

        #해당노드에서의 경로 추적
        print("="*20)
        print(data_array[node_num])
        print("="*20)
        for data in data_array[node_num]:
            #data[0] 넥스트노드 번호
            #data[1] 비용
            heapq.heappush(h,(data[1],data[0]))

            #현재 최소경로값이 거친경로 + 현재비용 보다 크다면 업데이트
            if shortway_array[data[0]] > shortway_array[node_num] + data[1] :
                shortway_array[data[0]] = shortway_array[node_num] + data[1]
        
        print(shortway_array[1:])

input_array = [
    [1,2,2],
    [1,3,5],
    [1,4,1],
    [2,3,3],
    [2,4,2],
    [3,2,3],
    [3,6,5],
    [4,3,3],
    [4,5,1],
    [5,3,1],
    [5,6,2]
]

INF = 1000000

data_array = [[] for _ in range(7)]
visited_array = [False] * 7
shortway_array = [INF] * 7

for i in input_array:
    #i[0] 노드번호
    #i[1] 이동노드번호
    #i[2] 비용
    data_array[i[0]].append((i[1],i[2]))

start(1)

#print(data_array)
#print(shortway_array[1:])
#print(visited_array[1:])