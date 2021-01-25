import time

start_time = time.time()
#구현 시작
'''
1초
0 <= n,m <= 1000
뚫린부분 0 막힌부분 1
input : 
4 5
00110
00011
11111
00000
        
output : 3
'''
icecream_cnt = 0
def count_icecream(position,visited,n,m,start_pos):
    global icecream_cnt
    #          L R U D
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]

    print(start_pos)
    #시작점이 아이스크림자리(0) 인지 확인후 카운트
    if pos[start_pos[0]][start_pos[1]] == str(0):
        icecream_cnt += 1
        visited[start_pos[0]][start_pos[1]] = icecream_cnt

    #이동 시키기
    for i in range(4):
        


    print(visited)

n = 4
m = 5
pos = ["00110","00011","11111","00000"]
position = [list(row) for row in pos]

#visited = [[0]*5]*4
visited = [[0 for col in range(m)] for row in range(n)]

start_pos = (0,0)

count_icecream(position,visited,n,m,start_pos)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
