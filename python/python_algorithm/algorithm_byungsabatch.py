'''
input : 
7
15 11 4 8 5 2 4
output:
2

n명의 병사중 뒤병사보다 전투력이 낮은 병사를 열외시켜 정렬
남은 병사의수가 최대가 되도록
'''
input_array = [15,11,4,8,5,2,4]

data_array = []
cnt=0
for i in range(len(input_array)):
    if i != 6:
        if input_array[i] > input_array[i+1]:
            data_array.append(input_array[i])
        else:
            cnt+=1

print(data_array)
print(cnt)