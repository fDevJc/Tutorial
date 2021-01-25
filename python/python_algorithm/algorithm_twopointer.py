'''
투포인터 알고리즘
'''
def prefix_sum(start_idx,end_idx):
    pr_sum = 0
    for i in range(start_idx,end_idx+1):
        pr_sum += input_list[i]
    
    return pr_sum

input_list = [1,2,3,2,5]

start_idx = 0
end_idx = 0

m = 5

while start_idx != (len(input_list)):
    
    pr_sum = prefix_sum(start_idx,end_idx)
    if pr_sum == m:
        print("정답 : ",start_idx," : ",end_idx)
        start_idx+=1
    elif pr_sum < m:
        end_idx += 1
    else:
        start_idx +=1


