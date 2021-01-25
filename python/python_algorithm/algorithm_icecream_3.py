import time

cnt = 0
b = True

def print_list(list):
    print("="*10)
    for row in list:
        print(row)
    print("="*10)        

def make_icecream(icecream_board, icecream_num, cur_r_pos, cur_c_pos):
    global cnt
    global b
    cnt +=1
    print(cnt)
    if cnt >25:
        b = False
    '''
    if 현재위치에 아이스크림을 담을수있을때
        if 해당위치 lrud 에 이미 아이스크림이 있을때
            근처에 위치해있는 아이스크림 덩어리번호의 맥스값을 해당좌표 아이스크림값에 대입
        else 아이스크림이 없을때
            새로운 아이스크림 번호를 대입

    다음좌표로 이동(오른쪽)
    c+1
    '''
    #          L R U D
    move_c = [-1,1,0,0]
    move_r = [0,0,-1,1]    

    if icecream_board[cur_r_pos][cur_c_pos] == 0:   #현재아이스크림 보드에 아이스크림을 담을수 있을때
        max_icecream_num = 0
        for i in range(4):
            chk_r_pos = cur_r_pos + i
            chk_c_pos = cur_c_pos + i

            if (0 <= chk_r_pos <=3) or (0 <= chk_c_pos <=4): #네방향 확인 후 맥스값이 있으면 맥스값 대입
                if icecream_num > max_icecream_num:
                    max_icecream_num = icecream_num

        icecream_num[cur_r_pos][cur_c_pos] = max_icecream_num                    
    #다음좌표이동
    if cur_c_pos >= 5:
        cur_c_pos = 0
        cur_r_pos += 1
    if cur_r_pos <= 4 and b:
        make_icecream(icecream_board,icecream_num,cur_r_pos,cur_c_pos)

start_time = time.time()
#구현 시작
n = 4
m = 5
input_pos = ["00110","00011","11111","00000"]
#아이스크림 판
icecream_board = [list(row) for row in input_pos]
#아이스크림을 담을수있는지 확인 0 못담음 >=1 덩어리수
icecream_num = [[0 for col in range(m)] for row in range(n)]

#최초 행 위치
cur_r_pos = 0
#최초 열 위치
cur_c_pos = 0

make_icecream(icecream_board,icecream_num,cur_r_pos,cur_c_pos)

print_list(icecream_board)
print_list(icecream_num)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)