# -*- coding: UTF-8 -*-
#copyright ： Peterpei 2020 - 2020 version2
import os.path#规避可能发生的找不到文件问题
import time
import  os
import  json
import  pyautogui #点击事件
lastJson = 0
rantime = 0.5

#读取用户自定设置
scriptpath = os.path.dirname(__file__)
userfilename = os.path.join(scriptpath, 'user.json')
userjson =open(userfilename, encoding = "utf-8", mode="r")
userjson1 = userjson.read()
userJsonDict = json.loads(userjson1)
rolltime = userJsonDict["rolltime"]

def openjsonfile():#打开文件
    filename = os.path.join(scriptpath, 'ThisDataPacketBody.json')
    openfile=open(filename, encoding = "utf-8", mode="r")
    GetJson = openfile.read()
    JsonDict = json.loads(GetJson)
    global Data
    Data = JsonDict["data"]#选取源json文件中data部分，继续解析
    openfile.close()
    return Data

def judgetype(Data):#解析题型
    AnswerTypeselect = 'options' in Data.keys() #选择
    AnswerTypeMultiSelect = 'chance_num' in Data.keys()#多选
    AnswerTypeMultiCombine = False
    judgecombine1 = 'stem' in Data.keys()
    str1 = '_'
    if judgecombine1 == True:
        str2 = Data["stem"]["content"] 
        judgecombine2 = str1 in str2
        if judgecombine2 == True:
            AnswerTypeMultiCombine = True#多选词组
    return AnswerTypeselect , AnswerTypeMultiSelect , AnswerTypeMultiCombine 

def fillchart(Data , rantime):#填空题
    answer = Data["answer_content"]
    answerLen = len(answer)
    questionDir = Data["stem"]
    question = questionDir["content"]
    QuestionLeng = len(question)
    listQuestion = list(question)
    findLeng = 0
    while (findLeng < QuestionLeng) :
        if listQuestion[findLeng] == '{' :
            break
        findLeng = findLeng + 1
        
    print   (findLeng)
    if  findLeng < 45:
        xPosion =  35 + findLeng * 15 + answerLen
        yPosion = 225
    else:
        xPosion = ( findLeng - 45 ) * 10 + 35
        yPosion = 225 + 40 
    time.sleep(rantime)#停止点击
    pyautogui.click(x=xPosion, y=yPosion, clicks=1, button='left')
    pyautogui.typewrite(answer)
    pyautogui.click(x=250, y=450, clicks=1, button='left')
    time.sleep(rantime)#停止点击
    pyautogui.click(x=450, y=1000, clicks=1, button='left')

def singleSelect(Data , rantime):#单选{普通单选 语音单选}
    Options = Data["options"]
    questionDir = Data["stem"]
    question = questionDir["content"]#拿题目长度
    #获取正确选项
    #lengthNums = len(question)
    a = 0
    i = 0    
    while (a < 3):
        if Options[i]["answer"] == True:
            break
        else:
            i = i + 1
            a = a + 1
    ansy = 0
    #对题目长度进行分类讨论和适配
    #重写对行数的函数
    length = len(question)
    print   ("正确答案是",Options[i]["content"])
    print   ("题目数目",length)
    a = 0 #问题在于单词是连续的，不能一个单词显示两行..
    while (a < 8):
        if a * 45 < length <= (a + 1) * 45:
            lengy = a + 1
            if 0< length < 20:
                lengy = 1.5
        a = a + 1

        #第一个数值是初始顶端到第一个选项中心的高度 第二个是各选项中心高度差 第三个是描述题目行数高度
        #来源1920 x 1080 的数据.
    if i == 0:
        ansy = 260 + 70*(i+1) + 45*(lengy -1)
    elif i == 1:
        ansy = 260 +70*(i+1) +45*(lengy -1)
    elif i == 2:
        ansy =260 + 70*(i+1) + 45*(lengy -1)
    elif i == 3:
        ansy=260 + 70*(i+1) + 45*(lengy -1)
        #pyautogui.moveTo(x=300, y=ansy)
    pyautogui.click(x=300, y=ansy, clicks=1, button='left')
    time.sleep(rantime)#停止点击
    pyautogui.click(x=450, y=1000, clicks=1, button='left')
    print   ("判断的行数",lengy)

def multiSelect(Data , rantime):#多选题
    Options = Data["options"]        
    #answerNum = Data["answer_num"]#答案数量
    Selections = 0 
    X = 35 
    Y = 430
    lenselections = len(Options)
    while  (Selections < lenselections):
        if Options[Selections]["answer"] == True :
            pyautogui.click(x=X, y=Y, clicks=1, button='left')
            print   ("正确选项是",Options[Selections]["content"])

        X = len(Options[Selections]["content"])*15 + 50 + X
            
        if Selections == lenselections - 1:
            Selections = lenselections -1
            break
        else:    
            Selections = Selections + 1  
        #对多选逻辑进行判断
        if X + len(Options[Selections]["content"])*15 + 50 > 500:
            X = 35
            Y = Y + 75
    time.sleep(rantime)#停止点击
    pyautogui.click(x=450, y=1000, clicks=1, button='left')    

def multicombine(Data , rantime):#链接词组题
    selectnums = Data["stem"]
    content = selectnums["content"]
    contentleng = len(content)
    print  (contentleng)
    judgeIf = '.'
    if judgeIf in content:
        elements =(contentleng - 1 - 6) / 2 + 1
    else:
        elements = (contentleng - 1) / 2 + 1#词达人的同学你好，这也是你们的意料之中?
    a = 0
    while (a <= 3):
        if a*4 < elements <= (a + 1)*4 :
            length = a 
            print   ("行数是",length + 1)
        a = a + 1
    #拿到一共需要选几个
    answerContent = Data["answer_content"]
    answer = answerContent["answer_arr"]
    Options = Data["options"]
    lengans = len(answer)
    roll1 = 0
    roll2 = 0
    while (roll2 < lengans):
        if answer[roll2] == Options[roll1]["content"] :
            click = roll1 + 1
            if click % 2 == 1 :
                X = 150 
            else:
                X = 350
            Y = ( roll1 // 2 ) * 70 + 500 + length*70
            print   ("答案是",answer[roll2])
            pyautogui.click(x=X, y=Y, clicks=1, button='left')
            roll2 = roll2 + 1
            roll1 = 0
        else:
            roll1 = roll1 + 1
    time.sleep(rantime)#停止点击
    pyautogui.click(x=450, y=1000, clicks=1, button='left')

#主函数
roll = 0
while (roll < rolltime):
    Data = openjsonfile()
    if lastJson == Data :
        bugreport = bugreport + 1
        if bugreport > 2:
            print   ("程序出了些问题...终止循环")
            break
    else:
        lastJson = Data
        bugreport = 0

#select = judgetype(Data)[0] multi = judgetype(Data)[1] combine = judgetype(Data)[2]
    if judgetype(Data)[0] == False:
        fillchart(Data , rantime)

    elif judgetype(Data)[0] == True and judgetype(Data)[1] == False and judgetype(Data)[2] == False:
        singleSelect(Data , rantime)

    elif judgetype(Data)[0] == True and judgetype(Data)[1] == True:
        multiSelect(Data , rantime)

    elif judgetype(Data)[2] == True:
        multicombine(Data, rantime)

    roll = roll + 1
