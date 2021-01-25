import time

start_time = time.time()

#------input--------------------------
# 1<= n <= 100000 시간제한 1초
n = 8
warriors = [2,3,1,2,2,5,8,5]
#-------------------------------------
#공포도가 낮은 모험가부터 정렬
cnt = 0
warriors.sort()

#팀들의 배열 생성
teams = []

#각 모험가 확인
#들어갈팀이 있는지 확인
for p in warriors:
    #팀이 하나도 없다면 팀을 생성
    #0번 인덱스 (최근만들어진 팀)에 자리가 있는지 확인
    #0번 인덱스 팀의 인원과 해당팀의 맥스 공포도가 같으면 팀을 생성
    if (len(teams) ==0) or (len(teams[0]) == max(teams[0])):
        new_team = []
        teams.insert(0,new_team)
        cnt+=1
    teams[0].insert(0,p)

'''
#만들어진 팀 검사
for team in teams:
    if len(team) >= max(team):
        cnt += 1

'''
print(cnt)
print(teams)


    
end_time = time.time()

print("동작시간 : ", end_time-start_time)
