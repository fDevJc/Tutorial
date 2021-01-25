n = 26

#2부터 n까지의 모든 자연수 나열
num_list = []
for i in range(2,n+1):
    num_list.append(i)

#2부터 n까지의 소수판별 배열
sosu_list = [True] * (n-1)

for i in range(len(num_list)):
    #num_list[i] : 2~26
    #sosu_list[i] : 소수 여부판별
    if sosu_list[i] == False:
        continue

    for j in range(len(num_list)):
        if num_list[i] == num_list[j]:
            continue
        else:
            if num_list[j] % num_list[i] == 0:
                sosu_list[j] = False

for i in range(len(num_list)):
    print(num_list[i]," : ",sosu_list[i])