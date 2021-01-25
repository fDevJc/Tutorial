'''
input:
3 4
1 3 3 2
2 1 4 1
0 6 4 7

output:
2+6+4+7 = 19
'''

row = 3
col = 4
data_array = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]
#빈배열 만들기
sum_array = [[0]*col for _ in range(row)]

for c in range(col):
    for r in range(row):
        #print("r : ",r , " c: ", c, end=' ')
        if c == 0:
            sum_array[r][c] = data_array[r][c]
        else:
            sum_array[r][c] = sum_array[r][c-1] + data_array[r][c]
            
            if 0 <= r-1 <= row-1:
                sum_array[r][c] = max(sum_array[r][c] , sum_array[r-1][c-1]+data_array[r][c])

            if 0 <= r+1 <= row-1:
                sum_array[r][c] = max(sum_array[r][c] , sum_array[r+1][c-1]+data_array[r][c])


for i in sum_array:
    print(i)

