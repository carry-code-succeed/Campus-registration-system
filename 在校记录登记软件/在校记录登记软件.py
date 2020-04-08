import wx
import datetime

student=[] #存放数据
def addStu(a,b,c):
    for i in range(0,len(student)):
        if(a==student[i][0]):
            return student

    info=[a,b,c,'']
    student.append(info)
        
def paixu(djb):       #排序功能       #djb=登记表
    djb.sort(key=lambda djb:djb[0])     #通过lambda函数按第0列排序
    #     print(djb)            #测试，打印列表
    return djb           #返回djb登记表

def display(g):
    #排序函数
    paixu(g)
    b=''
    for i in range(len(g)):
        b=b+" ".join(g[i])+"\n"
    return b
            
def Stuleave(name,num,time):
    for i in range(0,len(student)):
        if((student[i][1]==name) & (student[i][0]==num)):
            student[i][3]=time
            message='姓名：'+name+' 学号：'+num+' 离开校园时间：'+time1_str
            return message
        else:
            message="查无此人"
            return message

def StuNumFind(list,num):
    f = 0     #标记
    n = len(list)  #统计数组行
    a=''
    for i in range(n):   #行循环
        if(list[i][0]==num):
            f =1         #表明查找到学号
            a='找到此学生，信息如下：'+'\n'+'学号：'+list[i][0]+'姓名：'+list[i][1]+'进来时间:'+list[i][2]+'出去时间:'+list[i][3]
            break
            
    if(f==0):
        return '没有此学生姓名，查询失败'
    else:
        return a
        
        
def searchName(list,num):
    leap=0
    for i in range (len(list)):
        if list[i][1]== num:
                leap=1
                break
    if leap==0:
        a="没有此学生姓名，查询失败"
    else:
        a='找到此学生，信息如下：'+'\n'+'学号：'+list[i][0]+'姓名：'+list[i][1]+'进来时间:'+list[i][2]+'出去时间:'+list[i][3]
    return a
    

class MyFrame(wx.Frame):
    def __init__(self,  parent,  id):
        wx.Frame.__init__(self,  parent,  id,  '校园进出登记',  size=(500,  300))
        # 创建面板
        panel = wx.Panel(self)

        # 创建按钮, 并绑定事件
        self.bt_confirm = wx.Button(panel,  label='进入校园')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel,  label='离开校园')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        self.bt_xianshi = wx.Button(panel,  label='显示信息')
        self.bt_xianshi.Bind(wx.EVT_BUTTON, self.OnclickXianshi)
        self.bt_xue = wx.Button(panel,  label='按学号查找')
        self.bt_xue.Bind(wx.EVT_BUTTON, self.OnclickXue)
        self.bt_xing = wx.Button(panel,  label='按姓名查找')
        self.bt_xing.Bind(wx.EVT_BUTTON, self.OnclickXing)
        # 创建文本，左对齐        
        self.title = wx.StaticText(panel,  label="请输入姓名和学号")
        self.label_user = wx.StaticText(panel,  label="姓名:")
        self.text_user = wx.TextCtrl(panel,  style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel,  label="学号:")
        self.text_password = wx.TextCtrl(panel,  style=wx.TE_LEFT)
        # 添加容器，容器中控件按横向并排排列
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,  proportion=0,  flag=wx.ALL,  border=5)
        hsizer_user.Add(self.text_user,  proportion=1,  flag=wx.ALL,  border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,  proportion=0,  flag=wx.ALL,  border=5)
        hsizer_pwd.Add(self.text_password,  proportion=1,  flag=wx.ALL,  border=5)
        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.bt_confirm,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        hsizer_button.Add(self.bt_cancel,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        hsizer_button.Add(self.bt_xianshi,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        hsizer_button.Add(self.bt_xue,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        hsizer_button.Add(self.bt_xing,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,  proportion=0,  flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, 
                        border=15)
        vsizer_all.Add(hsizer_user,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        vsizer_all.Add(hsizer_pwd,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        vsizer_all.Add(hsizer_button,  proportion=0,  flag=wx.ALIGN_CENTER | wx.TOP,  border=5)
        panel.SetSizer(vsizer_all)
        
   
            
            
    def OnclickSubmit(self, event):
        """ 点击进入校园按钮，执行方法 """
        message = ""
        name = self.text_user.GetValue()     # 获取输入的姓名
        no = self.text_password.GetValue()  # 获取输入的学号
        time1 = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
        
        if name == "" or no == "":    # 判断姓名或学号是否为空
            message = '姓名或学号不能为空'
            
        else:
            message = '姓名：'+name+' 学号：'+no+' 进入校园时间：'+time1_str   
            addStu(no,name,time1_str)
            
        wx.MessageBox(message)                        # 弹出提示框          

    def OnclickCancel(self, event):  
        """ 点击离开校园按钮，执行方法 """
        message = ""
        name = self.text_user.GetValue()     # 获取输入的姓名
        no = self.text_password.GetValue()  # 获取输入的学号
        time1 = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M:%S')
        if name == "" or no == "":    # 判断姓名或学号是否为空
            message = '姓名或学号不能为空'
        else:
#             message = '姓名：'+name+' 学号：'+no+' 离开校园时间：'+time1_str   
            message=Stuleave(name,no,time1_str)
        wx.MessageBox(message)
        
    def OnclickXianshi(self, event):
        """ 点击查看信息按钮，执行方法 """
        message = ""
        message =display(student)
        wx.MessageBox(message)
    
    def OnclickXue(self, event):
        no = self.text_password.GetValue()  # 获取输入的学号
        
        message = ""
        message=StuNumFind(student,no)
        wx.MessageBox(message)
        
    def OnclickXing(self, event):
        name = self.text_user.GetValue()     # 获取输入的姓名
        
        message = ""
        message =searchName(student,name)
        wx.MessageBox(message)
        
if __name__ == '__main__':
    app = wx.App()                      # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数    
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法
