#xiaotang test git
#无返回值，有参数, 默认返回None
def func1(name):
    print(name)

#有返回值，无参数
def func2():
    print("有返回值，无参数")
    return 1

#有参数有返回值    
def func3(name):
    return name

if __name__ == '__main__':
    func1("lili")
    func2()
    func3("小唐")
