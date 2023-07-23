"""
字符串格式化除了可以用% 也可以用format()

内置函数：
name.capitalize() 首字母大写
name.count('x') 查找x出现的次数
name.find('x') 查找第一次出现的位置，返回下标，-1为不存在
name.index('x') 同find,但是不存在会报错
name.replace(old,new) 查找替换

name.strip() 去空格和换行符,可指定
去掉左边或者右边的空格/换行符:
name.lstrip()
name.rstrip()

判断大小写

拼接切割：split() join()
"""
A = "abc bcd cdb"
A.split()
print(A)
print('123'.join(A))

"""
format()方法的优点有哪些？
1.无须理会数据类型的问题,在%方法中%s只能替代字符串类型
2.单个参数可以多次输出，参数顺序可以不相同
3.填充方式十分灵活，对齐方式十分强大

python中为什么会出现中文乱码？
在Python中提到unicode，一般指的是unicode对象，
而str是一个字节数组，这个字节数组表示的是对unicode对象编码（可以是utf-8、gbk、cp936、GB2312）后的存储的格式。
这里它仅仅是一个字节流，没有其他的含义，如果想使这个字节流显示的内容有意义，就必须用正确的编码格式，解码显示。
对于unicode对象进行编码，编码成一个utf-8编码的str－如s_utf8，s_utf8就是一个字节数组，
print语句的实现是将要输出的内容传送给操作系统，
操作系统会根据系统的编码对输入的字节流进行编码，因为编码用GB2312去解释，其显示出来就错误了。
"""

"""
切片：
序列名[起始索引:终止索引:步长]
"""
list1 = [1, 2, 3, 'a', 'b', 'c']
print(list1[0:4:3])
print(type(list1[0:4:3]))
list2 = ['g', 'h', 'l']
# 拼接序列用+。重复序列用*
print(list1+list2)
print(list1*2)
"""
in() not in()查询元素是否在序列中，返回布尔值
len() 长度
min() max() 最大最小
sum() 计算元素只为数值的序列和
"""
# 除了直接创建，也可以用list()创建列表，这个有点像强制类型转换
list3 = list('ABC')
# 增加元素
list1.append(100)
# 拼接
list1.extend(list2)
# 指定位置插入元素
list1.insert(0, 1000)
# 删除元素
del list1[0]
# 获取并删除
list1.pop(0)
# 指定元素删除
list1.remove('a')
# 复制
list4 = list1.copy()
# 查询元素索引
list1.index('b')

# 元组，圆括号，不可修改但是提取和切片都可以，只有一个元素时也要加逗号
tuple1 = (1, 2, 3, 4)
tuple2 = tuple((6, 7, 8))
# 解包，用元组给多个变量一次性赋值
a, b, c, d = tuple1
print(a, b, c, d)
# +,* 操作同上,len 长度 sorted 排序 tuple.count() 记录某个元素出现的次数 tuple.index() 某个元素第一次出现的位置

# 字典，键唯一且不可变，键值可以重复,创建方式还是有2种
dict1 = {'name': 'zhangsan', 'age': 7, 'class': 'first'}
# 获取键值
print(dict1['age'])
# 增加新的键值对
dict1['school'] = '123'
print(dict1)
# 删除 ,删除整个字典用del dict1
del dict1['school']
print(dict1)
# 遍历
for k in 'age':
    print(k)
for k in dict1.values():
    print(k)
for k in dict1.keys():
    print(k)
for (k, v) in dict1.items():
    print(k, v)
# 打印所有项
print(list(dict1.items()))
print(list(dict1.keys()))
print(list(dict1.values()))
