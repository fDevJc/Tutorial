import time

cnt = 0
b = True
g_max_icecream_num = 0

def print_list(list):
    print("="*10)
    for row in list:
        print(row)
    print("="*10)        

def make_icecream(icecream_board, icecream_num, cur_r_pos, cur_c_pos):
    global g_max_icecream_num
    #          L R U D
    move_c = [-1,1,0,0]
    move_r = [0,0,-1,1]    
    #                   0           4
    if icecream_board[cur_r_pos][cur_c_pos] == "0":   #현재아이스크림 보드에 아이스크림을 담을수 있을때
        chk_max_yn = False
        max_num = 0
        print("(cur_r_pos : ",cur_r_pos," cur_c_pos : ", cur_c_pos ,") max_icecream_num : ",g_max_icecream_num)
        for i in range(4):
            chk_r_pos = cur_r_pos + move_r[i]
            chk_c_pos = cur_c_pos + move_c[i]

            if (0 <= chk_r_pos <=3) and (0 <= chk_c_pos <=4): #네방향 확인 후 맥스값이 있으면 맥스값 대입
                #0이 아닌값이 있으면 
                if icecream_num[chk_r_pos][chk_c_pos] != 0:
                    chk_max_yn = True
                    max_num = icecream_num[chk_r_pos][chk_c_pos]
                    break
                #주변숫자가 다 0이면
                else:
                    chk_max_yn = False
                    
        if chk_max_yn:
            icecream_num[cur_r_pos][cur_c_pos] = max_num
        else:
            g_max_icecream_num +=1
            icecream_num[cur_r_pos][cur_c_pos] = g_max_icecream_num
        
        '''                    
        with open(file = "test.txt",mode="a",encoding="utf-8") as f:
            f.write("cur_r_pos : "+str(cur_r_pos)+" cur_c_pos : "+str(cur_c_pos)+"max_icecream_num : "+str(max_icecream_num)+"\n")
        '''
        
    #다음좌표이동
    if cur_c_pos >= 4:
        cur_c_pos = 0
        cur_r_pos += 1
    else:
        cur_c_pos += 1
    if cur_r_pos <= 3:
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