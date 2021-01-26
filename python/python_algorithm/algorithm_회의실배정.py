'''
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 
시작 시간과 끝나는 시간은 2**31-1보다 작거나 같은 자연수 또는 0이다.

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
#입력받은 회의 개수
n = int(input())
#입력받은 회의 시간
meeting_time_list = [] * n
# 0 ~ 23 시간 빈 배열 - 예약여부 넣기
reservation_time_list = [False] * 1000000


for i in range(n):
    dp = tuple([int(i) for i in input().split(" ")])
    meeting_time_list.append(dp)

#입력받은 회의 시간 짧은 순서로 정렬
sorted_meeting_time_list = sorted(meeting_time_list,key=lambda time : time[1] - time[0])

#최종 회의 갯수
total_meeting_cnt = 0

#회의 시간이 짧은 순서로 예약
for meeting_start_end_time in sorted_meeting_time_list:
    # meeting_start_end_time[0] 시작시간
    # meeting_start_end_time[1] 종료시간

    #만약 회의 시작시간과 종료시간이 동일한경우 시작하자마자 끝나는 경우이기때문에 카운트 +1
    if meeting_start_end_time[0] == meeting_start_end_time[1]:
        total_meeting_cnt += 1
        continue

    #시작시간부터 종료시간까지 미리잡혀있는 회의시간이 없으면 예약
    #미리 잡혀있는 회의시간 있는지 확인
    reservation_chk = False

    for meeting_time in range(meeting_start_end_time[0],meeting_start_end_time[1]):
        #시작시간 ~ 종료시간 사이에 예약된 시간이 존재한다면
        if reservation_time_list[meeting_time] :
            reservation_chk = True
            break

    #예약이 존재하는 것
    if reservation_chk:
        continue
    #예약이 존재하지 않으면 예약
    else:
        for meeting_time in range(meeting_start_end_time[0],meeting_start_end_time[1]):
            reservation_time_list[meeting_time] = True
        total_meeting_cnt +=1


print(total_meeting_cnt)

