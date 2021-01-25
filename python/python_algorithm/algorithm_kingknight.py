import time

start_time = time.time()
#구현 시작
'''
8*8 1 ~ 8 , a ~ h
a,1 b,1 c,1
a,2 b,2 c,2 ....

1초
input : a1
        
output :2
'''
input_str = "a1"

x_positions = list("abcdefgh")
y_positions = list("123455678")

x = [idx for idx,i in enumerate(x_positions) if i==input_str[0]][0]
y = [idx for idx,i in enumerate(y_positions) if i==input_str[1]][0]

cnt = 0

if y - 2 >= 0:
    if x - 1 >= 0:
        cnt +=1
    elif x + 1 <= 7:
        cnt +=1
elif y + 2 <= 7:
    if x - 1 >= 0:
        cnt +=1
    elif x + 1 <= 7:
        cnt +=1

if x + 2 <= 7:
    if y - 1 >= 0:
        cnt +=1
    elif y + 1 <= 7:
        cnt +=1
elif x - 2 <= 7:
    if y - 1 >= 0:
        cnt +=1
    elif y + 1 <= 7:
        cnt +=1

print(cnt)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
