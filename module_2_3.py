my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
len_list= len(my_list)
while True:
    if my_list[a]>=0:
        print(my_list[a])
        if my_list[a] < 0:
            break
        a = a + 1
        if len_list > a:
            continue
    if len_list == a:
        break

