'''
바이너리 인덱스 트리 (Binary Index Tree)
'''

def prefix_index_binary_tree(data_array) :
    index_array = [i for i in range(len(data_array)+1)]

    for i in data_array:
        lsd = i & -i
        data_sum = 0
        print(lsd)
        for j in range(i,i-lsd,-1):
            data_sum+=j
        index_array[i] = data_sum
    return index_array


n = 16

data_array = [i for i in range(n+1)]

index_array = prefix_index_binary_tree(data_array)

print(index_array)

