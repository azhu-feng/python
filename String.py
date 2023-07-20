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