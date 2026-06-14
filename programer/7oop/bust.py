class student:
    StudentList = {}
    def __init__(self,name:str,ChineseScores:int,MathScores:int,EnglishScores:int):
        '''
        :param name:姓名
        :param ChineseScores:语文成绩
        :param MathScores: 数学成绩
        :param EnglishScores: 英语成绩
        '''
        # 属性字段
        self.name = name
        self.scores = {'语文':ChineseScores,'数学':MathScores,'英语':EnglishScores}
        # id字段与静态量更新
        student.StudentList[self.name]=self
        return
    def __str__(self):
        return f'{self.name} {self.scores}'
# 增
    @staticmethod
    def AppendStudent():
        name, ChineseScores, MathScores, EnglishScores = input('请输入‘姓名 语文成绩 数学成绩 英语成绩’\n').split(' ')
        ChineseScores, MathScores, EnglishScores = int(ChineseScores), int(MathScores), int(EnglishScores)
        new_st = student(name, ChineseScores, MathScores, EnglishScores)
        return
# 删
    @staticmethod
    def DeleteStudent(name):
        student.StudentList.pop(name)
        return
# 改
    @staticmethod
    def Modify(name,**kw):
        for sc in kw:
            student.StudentList[name].scores[sc[0]] = sc [1]
        return
# 查
    @staticmethod
    def ShowAll():
        print("姓名 语文 数学 英语")
        for st in student.StudentList:
            print(student.StudentList[st])
        return
    @staticmethod
    def ShowStudent(name):
        print("姓名 语文 数学 英语")
        print(student.StudentList[name])
        return
# run
def Run():
    le = lambda: print('-------------------------')
    while(1):
        # 提示信息
        le()
        print('''
请输入功能号以执行
    1. 添加学生信息
    2. 删除学生信息
    3. 修改学生信息
    4. 查询学生信息
    5. 打印数据库信息 
其他任意输入：退出
        ''')
        le()
        # 输入与执行
        op = int(input())
        match op:
            case 1:
                student.AppendStudent()
                student.ShowAll()
            case 2:
                student.DeleteStudent(input('请输入要删除的学生信息的姓名'))
                student.ShowAll()
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                break


if __name__ == "__main__":
    Run()