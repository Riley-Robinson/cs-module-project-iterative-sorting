
#Did it with a anonymous function Riley

num_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


result = list(filter(lambda x: (x % 3 == 0), num_list))
print("Numbers divisible by 3 are",result)