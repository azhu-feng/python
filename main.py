import sys

print("hello world!")
# python是一种面向对象的语言
# python是一种解释型语言
"""
1.
Python是一种编程语言，
它有对象、模块、线程、异常处理和自动内存管理。
它简洁、简单、方便、容易扩展，有许多自带的模块，而且它开源。

2.
编译型语言程序在执行之前需要一个专门编译的过程。
把程序编译成机器语言运行时，不需要再重新翻译，直接使用编译结果。
程序执行效率高，依赖编译器跨平台性差，比如C/C++

解释型语言程序不需要编译程序。
在运行时才翻译成机器语言,每执行一次要翻译一次。
程序执行效率比较低。依赖解释器，跨平台性好，比如Python，JavaScript，shell.
"""
print(330+200)
# python中不用分号和大括号，而是用缩进表示包含关系
"""
代码换行：
1.末尾加 /
2.语句中包含[],(),{}换行不需要加换行符
3.采用三个单引号或者采用三个双引号，如下
"""
print('''我学'''
      '''python''')
print("""i learn """
      """python""")
# 代码并行:分号,冒号后面的缩进可以并行
# python中字符串的拼接用+
# if-elif-else
num = int(input("输入一个数字:"))
# 同步赋值,逗号后加空格
x = 0
y = 1
x, y = y, x
print(x, y)
# 关于print
print(sep=" ", end="\n", file=sys.stdout, flush=False)
"""
sep是多个参数间分隔符
end是输出结束时的字符
file是定义流输出的文件 eg.file = open('python.txt','a') //a表示打开文件方式为添加模式
flush判断是否立刻把内容输出到流文件，不做缓存
"""
print(1, 2, 3, 4, sep="&")
"""
什么是PEP8?
PEP8是一个编程规范，是可以使程序代码整洁美观，更具可读性的建议。
"""
