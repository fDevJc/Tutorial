n,k = map(int,input().split(" "))

items = []
dp= [0]*10

for i in range(n):
    items.append(tuple(int(x) for x in input().split(" ")))



for i in range(1,k+1):
    max=0
    print("")
    print("")
    for j in range(n): 
        print(f"{i}번째 for--------------------------------------------------------------------")
        print(f'1. 총무게i: {i} , 현제 아이템무게items[j][0]: {items[j][0]}')
        if i >= items[j][0]:
            p = i - items[j][0]; 
            print(f'2. p = i - items[j][0] /////// {p} = {i} - {items[j][0]}')
            res = dp[p] + items[j][1]
            print(f'3. res = dp[p] + items[j][1] //////// {res} = {dp[p]} + {items[j][1]}')
            print(f'4. res: {res} , max: {max}')
            if res>max:
                    
                max = res;
                dp[i] = max;
                print(f'5. dp[{i}] : {dp[i]}')
            
print(dp)
print(dp[k])
'''
4 6
6 13
3 8
7 15
2 6
'''