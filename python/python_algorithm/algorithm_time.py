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
with open(file="test.txt",mode="w",encoding="utf-8") as f:

    for h in range(0,n):
        for m in range(0,60):
            for s in range(0,60):
                if str(s).zfill(2)[1] == "3" or str(s).zfill(2)[0] == "3" or str(m).zfill(2)[1] == "3" or str(m).zfill(2)[0] == "3" or str(h).zfill(2)[1] == "3" or str(h).zfill(2)[0] == "3":
                    f.write("h:"+str(h)+" m:"+str(m)+" s:"+str(s) + "\n")
                    cnt += 1

print(cnt)
#구현 끝
end_time = time.time()
print("동작시간 : ", end_time-start_time)
