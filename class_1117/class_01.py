#对象object
#万物皆对象
#将有同特性的划分为一类


#自动化测试工程师类
#work_year=3
#salary=20000
#skill:写代码、会sql、会linux、会功能测试、会自动化测试、会接口测试


class ClassTest:  # 类的命名规则为驼峰，首字母大
    # 类的属性   属性值只能由对象调用
    name = 'chenting'
    age = 18
    group = 'python_12'

    # 对象方法  只能由对象调用
    def do_word(self):  # self表示对象，是一个占位符，标记这是一个对象方法，不起做作用，所有对象方法的第一个形参表示对象
        print('能写代码')

    # 静态方法，与正常的函数一样，如果是静态方法，不用占坑，需要用@staticmethod装饰
    #不能调用属性
    @staticmethod
    def do_fanction_testing():
        print('会功能测试')

    # 类方法   需要用@classmethod装饰
    @classmethod
    def do_sql(cls):  # 会传入一个类名，类似于self，于self的用法一样，类方法也需要一个占坑参数
        print('会操作数据库', cls.name)  # 用类名调用属性值

# 创建一个对象，变量名 = 类名（）
#类里面的函数，只允许对象调用
b1 = ClassTest()  # 一定带上（），才是对象,没有（）是类名
b1.do_word()  # 调用对象方法
b1.do_fanction_testing()  # 调用静态方法
b1.do_sql()  # 调用类方法
print(20 * '*')

b2 = ClassTest  # 不带（），只是一个类名
# b2.do_word() #报错，缺少一个对象方法self,TypeError: do_word() missing 1 required positional argument: 'self'
b2.do_word('self')  # 传入一个对象方法，可以正常调用
ClassTest().do_word()  # ClassTest()表示对象，可以正常调用
b2.do_fanction_testing()  # 调用静态方法，用类名调用
ClassTest().do_fanction_testing()  # 调用静态方法，用对象调用
b2.do_sql()  # 用类名调用类方法
ClassTest().do_sql()  # 用对象调用类方法

# 类里面的函数都可以用对象调用，对象方法只能用对象调用，静态方法和类方法可以用类名调用，也可以用对象调用