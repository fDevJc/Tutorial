from typing import Sequence
import random
import time
'''
4 7
2 13
4 8
1 6
3 12

5 10
1 1
1 2
1 3
1 4
1 5
'''
start_time = time.time()


def get_max_value(items:Sequence , bag_k:int, dp:Sequence,dp_in_k:Sequence):
    #1 부터 가방무게까지 각각의 무게의 합을 구한다
    for i in range(1,bag_k+1):
        print(f'{i}무게일때 --------------------------------------')

        max_v = 0

        for j in range(len(items)):
            print(f'{j}번째 아이템 무게:{items[j][0]} 가치:{items[j][1]}')

            if i >= items[j][0]:
                print(f'>> 가방무게:{i} >> ', end='')
                
                #현재 아이템을 가방에 넣고 남은 무게 계산
                remain_k = i - items[j][0]
                print(f' 잔여무게:{remain_k} ',end='')
                
                #현재아이템의 가치
                cur_item_v = items[j][1]
                print(f' 현재아이템의 가치 : {cur_item_v}',end='')
                
                #잔여무게의 가치
                remain_item_v = dp[remain_k]
                print(f' 잔여무게의 가치 : {remain_item_v}',end='')

                sum_v = remain_item_v
                tmp = dp_in_k[remain_k][:]
                if j not in dp_in_k[remain_k]:
                    sum_v += cur_item_v
                    print(f'  tmp에 {j}번째 아이템 삽입',end='')
                    tmp.append(j) 
                
                if sum_v > dp[i]:
                    dp[i] = sum_v
                    print(f' max_value : {dp[i]}',end='')
                    print(f'  << dp_in_k {i} 에 {tmp} 삽입 >>',end='')
                    dp_in_k[i].clear()
                    dp_in_k[i].extend(tmp)
                
                print()

            else:
                pass
        print(dp)
        print(dp_in_k)

'''
n , k = 4,7
items = [(2,13),(4,8),(3,6),(3,12)]
dp = [0] * (k+1)
dp_in_k = [[] for _ in range(k+1)]
'''
n,k = map(int,input().split(" "))
dp = [0] * (k+1)
dp_in_k = [[] for _ in range(k+1)]
items = []

for i in range(n):
    items.append(tuple(int(x) for x in input().split(" ")))

'''
n = random.randint(0,100)
k = random.randint(1,100000)
dp = [0] * k
items = []
for i in range(n):
    items.append(tuple([random.randint(1,100),random.randint(1,1000)]))

'''

get_max_value(items,k,dp,dp_in_k)
print(dp)
print(dp_in_k)

end_time = time.time()
print("동작시간 : ", end_time-start_time)