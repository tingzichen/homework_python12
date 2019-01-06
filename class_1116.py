class TestingTools:
    #属性
    name = '陈婷'
    age=18

    #方法，属于这一类的对象都拥有这些技能，这些方法，对象都可以用
    def do_sql(self):#这里的self实际是一个占坑符号，实际没有其他用处，但是属于这个类的方法都必须要加，可以不是self，默认第一个参数就是占坑符号，不是形参
        print(self)
        print('会操作sql')
    #此处应有静态参数，使该函数不属于这个对象，其他人也可以调用，静态参数下的函数，可以不用占坑符号self
    def do_shell():
        print('nihao ')

    def do_word(self,p):
        # print(self)
        print('会{0}语言'.format(p))

    def do_fanction_testing(self):
        print('会功能测试')

a1=TestingTools()
print(a1)
a1.do_fanction_testing()
a1.do_sql()
a1.do_word('python')
a1.do_shell()