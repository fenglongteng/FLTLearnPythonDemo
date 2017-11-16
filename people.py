from dog import Dog

class People(object):

    '''

        Python 用下划线作为变量前缀和后缀指定特殊变量

        _xxx 不能用’from module import *’导入

        __xxx__ 系统定义名字

        __xxx 类中的私有变量名

        核心风格：避免用下划线作为变量名的开始。

        因为下划线对解释器有特殊的意义，而且是内建标识符所使用的符号，我们建议程序员避免用下划线作为变量名的开始。
        一般来讲，变量名_xxx被看作是“私有的”，在模块或类外不可以使用。当变量是私有的时候，用_xxx 来表示变量是很好的习惯。
        因为变量名__xxx__对Python 来说有特殊含义，对于普通的变量应当避免这种命名风格。

        “单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；
        “双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。

        以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入；
        以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，
        如 __init__（）代表类的构造函数。
        '''


    def __init__(self,name,age):
        self._name = name
        self._age = age



    # __开头的变量表示绝对私有变量，外界、子类不能直接访问。_ 一个下划线开头表示私有变量，但是可以访问，只是大家约定俗成，当成私有变量（子类可访问），不轻易调用。
    @property
    def name(self):
        return self._name#这里设置的变量是私有变量，是为了避免self.name，循环调用。

    @name.setter
    def name(self,value):
        self._name = value

    def bug_dog(self):
        dog = Dog('小黄')
        self.dog = dog


#__name__，

#如果是放在Modules模块中，就表示是模块的名字；

#如果是放在Classs类中，就表示类的名字；

print(__name__)

xiaoMing = People('张强',32)

print(xiaoMing.name)

xiaoMing.bug_dog()

'''
由于主程序代码无论模块是被导入还是直接被执行都会运行，所以我们需要一种方式在运行时检测该模块是被导入还是被直接执行。
该方式也就是__name__系统变量。如果模块是被导入，__name__的值为模块名字；如果是被直接执行，__name__的值为"__main__"。

'''

#所以我们允许代码执行的时候 还是用  __name__ = '__main__' 判断下比较好

print(xiaoMing.dog.name)