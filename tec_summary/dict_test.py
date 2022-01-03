dict = {"a":1, "b":2}
cp_dict = {}

# 在for循环中完成对字典的赋值（复制）操作
for k, cp_dict[k] in dict.items(): pass
print(cp_dict)
# Output cp_dict： {'a': 1, 'b': 2}



# 上面的的操作可简化理解：定义两个循环变量，基于for循环实现变量赋值
k, v = 0, 0
for k, v in dict.items(): pass
print(f'k, v = {k}, {v}', end='\t')

# Output： k, v = b, 2


# print(cp_dict)

# lst = []
# set
# for cp_dict["a"] in dict.keys(): pass 

# print(cp_dict)