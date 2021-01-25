input_str = "K1KA5CB7"

str_lst = list(input_str)
num_sum = 0
new_lst = []
for i in str_lst:
    if i.isnumeric():
        num_sum += int(i)
    else:
        new_lst.append(i)

new_lst.sort()
new_lst.append(str(num_sum))

print(''.join(new_lst))

