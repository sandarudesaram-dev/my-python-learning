# list slicing #

print()

# list[start: stop: step]

# start = inclusive. if not specified, default is first element(inclusive)
# stop = exclusive. if not specified, default is last element(inclusive)
# step = default (1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7 ,8, 9]
print("my_list:", my_list)
print()

# index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# index   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

list1 = my_list[0: 4]
print("my_list[0:4]:", list1)

list2 = my_list[2: 8: 2]
print("my_list[2: 8: 2]:", list2)

list3 = my_list[: 5: 3]
print("my_list[: 5: 3]:", list3)

list4 = my_list[1::4]
print("my_list[1::4]:", list4)

list5 = my_list[::2]
print("my_list[::2]:", list5)

list6 = my_list[4:]
print("my_list[4:]:", list6)

list7 = my_list[:7:]
print("my_list[:7:]:", list7)

list8 = my_list[-9:-5]
print("my_list[-9:-5]:", list8)

list9 = my_list[3:-2]
print("my_list[3:-2]:", list9)

list10 = my_list[::-1]
print("my_list[::-1]:", list10)

list11 = my_list[::1]
print("my_list[::-1]:", list11)