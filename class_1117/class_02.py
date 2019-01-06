#函数内部之间的调用
class ClassTest:  #类的命名规则为驼峰，首字母大写

    #类的属性
    name ='chenting'
    age =18
    group ='python_12'

    #对象方法   对象方法里面调用其他方法
    def do_word(self):
        # self.do_linux()  #对象方法里面调用对象方法
        # self.do_fanction_testing()   #对象方法里面调用静态方法，对象方法.静态方法（）
        # self.do_sql() #对象方法里面调用类方法
        print('能写代码')

    # 对象方法
    def do_linux(self):
        print('会操作linux')


    #静态方法  静态方法里面调用其他方法
    @staticmethod
    def do_fanction_testing():
        # self.do_word()  #报错：NameError: name 'self' is not defined
        # ClassTest().do_word() #类里面，静态方法要想调用”对象方法“，必须要用   对象.对象方法()
        # ClassTest().do_tools()  #静态方法里面调用”静态方法“，可以用  对象.静态方法（）
        # ClassTest.do_tools()  #静态方法里面调用”静态方法“，也可以用   类名.静态方法（）
        # ClassTest().do_sql() #静态方法里面想调用”类方法“，可以用  对象.类方法()
        # ClassTest.do_sql()  #静态方法里面调用”类方法“，也可以用  类名.类方法()
        print('会功能测试')
        #静态方法里面，调用类里面其他的方法时，
        #1、调用“对象方法”时，必须要用对象调用
        #2、调用“静态方法”或“类方法”时，可以用对象调用，也可以用类名调用
        #另：在类外面调用“静态方法”或“类方法”时，也可以用对象调用，或者类名调用
        #在类外面调用对象方法时，必须要用对象调用


    #静态方法
    @staticmethod
    def do_tools():
        print('会用工具')

    #类方法   类方法里面调用其他方法
    @classmethod
    def do_sql(cls):
        ClassTest().do_word() #类方法里面调用“对象方法”时，必须要用对象调用，ClassTest()表示对象
        ClassTest().do_fanction_testing()  #类方法里面调用“静态方法”时，可以用对象调用
        cls.do_fanction_testing()  #类方法里面调用“静态方法”时，也可以用类名调用
        cls().do_sql_server()  #类方法里面调用“类方法”时，可以用对象调用
        cls.do_sql_server()  #类方法里面调用“类方法”时，可以用类名调用
        print('会操作数据库')

        #类方法里面，调用类里面其他的方法时，
        #1、调用“对象方法”时，必须要用对象调用
        #2、调用“静态方法”或“类方法”时，可以用对象调用，也可以用类名调用

    @classmethod
    def do_sql_server(cls):
        print('会操作sql_server数据库')


b1=ClassTest()
# b1.do_word() #调用对象方法
# b1.do_fanction_testing() #调用静态方法
b1.do_sql()  #调用类方法