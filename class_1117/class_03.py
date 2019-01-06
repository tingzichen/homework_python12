#初始化函数--出厂设置  设定的初始值  在创建的对象的时候必须要传参
class ClassTest:
    # 类的属性
    # name = 'chenting'
    # age = 18
    # group = 'python_12'
    def __init__(self,name,age,group):
        self.name=name
        self.age=age
        self.group=group

    # 对象方法
    def do_word(self):
        print('能写代码')
        print('{0}，年龄{1}岁，班级{2}'.format(self.name,self.age,self.group))

    # 静态方法
    @staticmethod
    def do_fanction_testing():
        print('会功能测试')

    # 类方法   需要用@classmethod装饰
    @classmethod
    def do_sql(cls):
        print('会操作数据库', cls.name)

#初始化函数--出厂设置  设定的初始值  在创建的对象的时候   必须要传参，相当于初始化了属性
b1 = ClassTest('chenting',18,'python_12')
b1.do_word()
#初始化函数，如果要调用静态方法或者类方法，就不用传很多参数，又用不上，直接   类名.函数名   就ok了
#学了初始化函数，明白了静态方法的必要性，当一个方法不需要用到类的属性的时候，就用静态方法吧
b2=ClassTest
b2.do_fanction_testing()