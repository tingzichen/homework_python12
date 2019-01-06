#异常处理
# 异常处理机制：抓到异常，然后做出相关处理
#try...except...
#try用来监控觉得可疑的代码
#如果用open（）打开文件，文件不会自动关闭，消耗内存，可以在open（）前面加with，用with open（）打开文件，操作完后，文件会自动关闭

# try:  #用来监测觉得可疑的代码
#     with open('python12.txt',encoding='utf-8') as file:#open（）打开时没有设置模式，这里默认是‘r’模式
#         file.write('python12真是666')
# except Exception as e: #处理错误，只有出现错误的时候，才会执行except 下面的代码
#     print('出错：{0}'.format(e))

# a=10
# try:
#     print(a+b)
# except TypeError as e:
#     print('出错：{0}'.format(e))
# finally: #finally下面放确认没有问题的代码，不管try下面的代码有没有问题都不影响finally下面代码的执行
#     c = 2
#     print(a + c)

a=10
try:
    print(a+b)
except NameError as e:
    print('出错：{0}'.format(e))
else: #只有当try里面的代码没有问题，才会执行else下面的代码
    c = 2
    print(a + c)




