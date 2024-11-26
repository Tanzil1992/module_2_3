my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
len_list= len(my_list)
while a < len_list:
    if my_list[a] > 0:
        print(my_list[a])
        if a + 1 == len_list:
            break
        else:
            a = a + 1
            continue
    if my_list[a] < 0:
        break
    a = a + 1



