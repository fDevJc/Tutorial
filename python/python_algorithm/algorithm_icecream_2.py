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
n = 4
m = 5
def count_icecream(position,visited,start_pos):
    global icecream_cnt
    #          L R U D
    move_x = [-1,1,0,0]
    move_y = [0,0,-1,1]

    #print(start_pos)

    continue_flag = True
    print("start_pos[0] : " , start_pos[0] , " start_pos[1] :",start_pos[1] )
    #현재위치가 아이스크림을 넣을수 없다면 현재좌표 이동
    if position[start_pos[0]][start_pos[1]] == 1:
        #x좌표 +1
        start_pos[1] += 1
        #x좌표가 5보다 크면 x좌표 0 y좌표 +1
        if start_pos[1] > 4:
            start_pos[1] = 0    
            start_pos[0] += 1
        #y좌표가 4보다 크면 종료
        if start_pos[0] > 3:
            continue_flag = False
        if continue_flag:
            count_icecream(position,visited,start_pos)
    #아이스크림을 넣을수 있다면 네방향 확인
    else : 
        l, r, u, d = 0, 0, 0, 0
        #왼쪽확인
        if start_pos[1] != 0:
            l = visited[start_pos[0]][start_pos[1]-1]
        #오른쪽확인
        if start_pos[1] != 4:
            r = visited[start_pos[0]][start_pos[1]+1]
        #위쪽확인
        if start_pos[0] != 0:
            u = visited[start_pos[0]-1][start_pos[1]]
        #아래쪽확인
        if start_pos[0] != 3:
            d = visited[start_pos[0]+1][start_pos[1]]
        
        if l == 0 and r ==0 and u==0 and d==0:
            icecream_cnt += 1
            visited[start_pos[0]][start_pos[1]] = icecream_cnt
        else:
            check = l,r,u,d
            visited[start_pos[0]][start_pos[1]] = max(check)
        #x좌표 +1
        start_pos[1] += 1
        #x좌표가 5보다 크면 x좌표 0 y좌표 +1
        if start_pos[1] > 5:
            start_pos[1] = 0    
            start_pos[0] += 1
        #y좌표가 4보다 크면 종료
        if start_pos[0] > 4:
            continue_flag = False
        if continue_flag:
            count_icecream(position,visited,start_pos)

    print(visited)


pos = ["00110","00011","11111","00000"]
position = [list(row) for row in pos]

#visited = [[0]*5]*4
visited = [[0 for col in range(m)] for row in range(n)]

start_pos = [0,0]

count_icecream(position,visited,start_pos)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)

