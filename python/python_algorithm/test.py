import sys
'''asdasdd'''

N = [int(x) for x in sys.stdin.readline().strip().split()][0]
time_list = [list(map(int, x.strip().split())) for x in sys.stdin.readlines()]
time_list = sorted(time_list,key = lambda x: x[1])
for i in range(len(time_list)-1):
    #  i번째 종료시간 == i+1번째 종료시간 and i번째 시작시간 > i+1 번째 시작시간 
    if time_list[i][1] == time_list[i+1][1] and time_list[i][0] > time_list[i+1][0]:
        time_list[i], time_list[i+1] = time_list[i+1], time_list[i]

print(time_list)

ans = 1
last_dsc = time_list[0]
print("last_dsc : ",last_dsc)
for dsc in time_list[1:]:
    print("dsc[0] >= last_dsc[1] : ",dsc[0] >= last_dsc[1])
    if dsc[0] >= last_dsc[1]:
        ans += 1
        last_dsc = dsc
print(ans)
