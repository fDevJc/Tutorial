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
cnt = 0

x = int(ord(input_str[0])) - int(ord("a")) + 1
y = int(input_str[1])



print(cnt)

#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
