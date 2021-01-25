import heapq
'''
n개의 도시가 있다
어느날 C도시에서 위급상황이 발생
최대한 많은 도시에 메시지를 보내려고 한다
각도시의 번호와 통로 정보가 주어졌을때
도시 C에서 보낸 메시지를 받은 도시의 개수 와
모두 메시지를 받는데 까지 걸린 시간은 얼마인지 구하시오
input:
3 2 1   도시의개수 통로의개수 도시C
1 2 4   X에서 Y로 이어진 통로가 있으며 전달시간 Z
1 3 2   X에서 Y로 이어진 통로가 있으며 전달시간 Z

output:
2 4
'''

def solve(start_city):
    #스타트 시티는 방문기록을 남기지 않음

    #출발노드에서 도착노드 탐색
    #data_list[start_city]  return [(도착노드,비용)....]

    h = []
    heapq.heappush(h,(0,1)) #(비용, 현재노드)

    while len(h):
        cost,cur_node = heapq.heappop(h)

        #방문지 방문 체크
        if visited_list[cur_node] : continue
        else : visited_list[cur_node] = True

        for data in data_list[cur_node]:
            #data[0] 도착노드
            #data[1] 비용
            if minway_list[data[0]] > data[1]:
                minway_list[data[0]] = data[1]
            
            heapq.heappush(h,(data[1],data[0]))
    
    

city_cnt = 7
#way_cnt = 2
start_city = 1

input_list  = [
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

data_list = [[] for _ in range(city_cnt+1)]

for i in input_list:
    #i[0] 출발노드
    #i[1] 도착노드
    #i[2] 비용
    data_list[i[0]].append((i[1],i[2]))

INF = 100000

visited_list = [False] * (city_cnt+1)
minway_list = [INF] * (city_cnt+1)

solve(start_city)

print(minway_list)
print(visited_list)