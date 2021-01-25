import time

start_time = time.time()
#구현 시작
'''
2초
1 <= n <= 100
1 <= 이동횟수 <= 100
input : 5
        R R R U D D
output : 3 4        
'''
n = 5
cur_x = 1
cur_y = 1
move_orders = ["R","R","R","U","D","D"]

for move_order in move_orders:
    if move_order == "R":
        if cur_x == n:
            continue
        cur_x += 1
    elif move_order == "L":
        if cur_x == 1:
            continue
        cur_x -= 1
    elif move_order == "U":
        if cur_y == 1:
            continue
        cur_y -= 1        
    elif move_order == "D":                
        if cur_y == n:
            continue
        cur_y += 1        

print(cur_y , cur_x)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
