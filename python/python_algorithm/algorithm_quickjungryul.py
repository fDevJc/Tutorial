def quick_sort(start_idx, end_idx,name,idx):
    print("quick_sort//","start_idx :",start_idx," end_idx :",end_idx," name :",name," idx :",idx,end=' ')
    print(input_array)
    if idx > 2:
        return False
    
    #print(input_array)
    pivot_idx = start_idx

    big_idx = 0
    small_idx = 0
    while True:
        #print(input_array)
        for i in range(start_idx,end_idx+1):
            if input_array[pivot_idx] < input_array[i]:
                big_idx = i
                break
        for i in range(end_idx,0,-1):
            if input_array[pivot_idx] > input_array[i]:
                small_idx = i
                break
        if big_idx > small_idx:
            print("겹침")
            input_array[pivot_idx] , input_array[small_idx] = input_array[small_idx] , input_array[pivot_idx]  
            #피벗으로 왼쪽
            if start_idx != end_idx:
                print("start_idx 와 end_idx 가 다를때 실행")
                quick_sort(start_idx,small_idx-1,"왼쪽",idx+1)
            #피벗으로 오른쪽
            quick_sort(small_idx+1,end_idx,"오른쪽",idx+1)
            break
        else:
            input_array[big_idx] , input_array[small_idx] = input_array[small_idx] , input_array[big_idx]


input_array = [5,4,9,0,3,1,6,2,7,8]

#print(input_array)
quick_sort(0,9,"최초",1)
#print(input_array)
