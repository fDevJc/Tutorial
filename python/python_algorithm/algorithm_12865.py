from typing import Sequence
import random
import time

def get_combination_max_value(p_arr:Sequence, max_v: int):
    #사용유무 배열
    useds = [0] * len(p_arr)
    #총 무게
    sum_w = 0
    #총 가치
    sum_v = 0
    #가치의 합 배열
    values = [0]
    def generate(arr,n,sum_w,sum_v,values):
        for i in range(n,len(p_arr)):
            
            if useds[i]:
                continue

            if sum_w + p_arr[i][0]> max_v:
                continue
            sum_w += p_arr[i][0]

            arr.append(p_arr[i])

            useds[i] = 1
            sum_v += p_arr[i][1]
            n+=1
            generate(arr,n,sum_w,sum_v,values)
            #print(arr,end = '')
            #print(" => ",sum_v)

            if sum_v > values[0]:
                values[0] = sum_v

            arr.pop()
            useds[i] = 0
            sum_w -= p_arr[i][0]
            sum_v -= p_arr[i][1]

    generate([],0,sum_w,sum_v,values)

    return values[0]

start_time = time.time()

'''
n,k = map(int,input().split(" "))

items = []

for i in range(n):
    items.append(tuple(int(x) for x in input().split(" ")))
'''


n = random.randint(0,100)
k = random.randint(1,100000)
items = []
for i in range(n):
    items.append(tuple([random.randint(1,100),random.randint(1,1000)]))

print(n,k)
print(items)

print(get_combination_max_value(items,k))


end_time = time.time()
print("동작시간 : ", end_time-start_time)



4 6

6 13

3 8

7 15

2 6

    for(int i=1;i<=K;i++){
        int max=0;

        for(int j=0;j<N;j++){
            if(i-arr[j][0]>=0){ // wholeWeight - itemWeight
                int p = i - arr[j][0]; 
                int res = dp[p] + arr[j][1]; //dp's maxValue + itemValue

                if(res>max){
                    //printf(" i:%dj%dr%d",i,j,res);
                    max = res;
                    dp[i] = max;
                }
            }
        }
    }