# coding=utf-8

class Employe(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        nameList = self.name.split()
        if isinstance(nameList, list):
            return nameList[0]

    def giveRaise(self,percent):
        if isinstance(percent,float):
            return float(self.pay * (percent + 1))

    # 重载 __str__() 方法
    def __str__(self):
        return "[Employe: %s,%s,%s]" %(self.name,self.job,self.pay)


class Manager(Employe):
    def giveRaise(self,percent,bouns=0.1):
        super().giveRaise(percent+bouns)

# 上面的if判断表示这个py文件如果当作可执行程序而不是模块，
# 则执行if内的语句，如果是以模块的方式导入这个文件，则if内的语句不执行。这种用法在测试模块代码的时候非常方便。
if __name__ == "__main__":
    longshuai = Employe("Ma longshuai")
    xiaofeng = Employe(name="Gao Xiaofeng", job="accountant", pay=18000)
    xuchuan = Manager(name="Xu Chuan",job="manager",pay=20000)

    print (xuchuan)

    print (longshuai.lastName())
    print (xiaofeng.giveRaise(0.2))
    print (xuchuan.giveRaise(0.3))

    print (object.__dict__["__str__"])