import time

start_time = time.time()
#구현 시작
'''
2초
0 <= n <= 23
1 <= 이동횟수 <= 100
input : 5
        
output :11475
'''

n = 5
cnt = 0
for h in range(0,n+1):
    for m in range(0,60):
        for s in range(0,60):
            if "3" in str(h)+str(m)+str(s):
                cnt +=1

print(cnt)
#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
