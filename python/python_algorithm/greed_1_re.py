n = 8
warriors = [2,3,1,2,2,5,8,5]

group_cnt = 0
group_person_cnt = 0

for w in warriors:
    group_person_cnt += 1
    if group_person_cnt >= w:
        group_cnt += 1
        group_person_cnt = 0

print(group_cnt)