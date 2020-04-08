# -*- coding: UTF-8 -*-
#copyright ： Peterpei 2020 - 2020
import  os
import  json
import  pyautogui #点击事件
roll = 0
lastJson = 0
bugreport = 0
while   (roll < 200):
    #解析json
    openfile = open("ThisDataPacketBody.json", mode="r", encoding="utf-8")#打开文件
    GetJson = openfile.read()
    JsonDict = json.loads(GetJson)
    Data = JsonDict["data"]#选取源json文件中data部分，继续解析
    #判断是否出现bug,由于点击事件太快导致脚本根本来不及响应.....增加bugreport计数，对太快响应导致的“bug”进行过滤
    if lastJson == Data :
        bugreport = bugreport + 1
        if bugreport > 3:
            print   ("Maybe something wrong.../Break the loop")
            break
    else:
        lastJson = Data
        bugreport = 0

    #分类题型
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


    if AnswerTypeselect == False:
        #填空题
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
        
        defaultX = 35
        print   (findLeng)
        if  findLeng < 45:
            xPosion =  35 + findLeng * 15 + answerLen
            yPosion = 225
        else:
            xPosion = ( findLeng - 45 ) * 10 + 35
            yPosion = 225 + 40 

        pyautogui.click(x=xPosion, y=yPosion, clicks=1, button='left')
        pyautogui.typewrite(answer)
        pyautogui.click(x=250, y=450, clicks=1, button='left')
        pyautogui.click(x=450, y=1000, clicks=1, button='left')

    elif AnswerTypeselect == True and AnswerTypeMultiSelect == False and AnswerTypeMultiCombine == False:
        #单选{普通单选 语音单选}
        Options = Data["options"]
        questionDir = Data["stem"]
        question = questionDir["content"]#拿题目长度
        #获取正确选项
        lengthNums = len(question)
        a = 0
        i = 0    
        while (a < 3):
            if Options[i]["answer"] == True:
                break
            else:
                i = i + 1
                a = a + 1
        x = 300
        ansy = 0
        #对题目长度进行分类讨论和适配
        #重写对行数的函数
        length = lengthNums * 10
        print   (Options[i]["content"])
        print   (length)
        a = 0 #问题在于单词是连续的，不能一个单词显示两行..
        while (a < 8):
            if a * 450 < length <= (a + 1) * 450:
                lengy = a + 1
                if 0< length < 300:
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
        pyautogui.click(x=450, y=1000, clicks=1, button='left')
        print   (lengy)
    
    elif AnswerTypeselect == True and AnswerTypeMultiSelect == True :
        #多选题
        #多选题每个选项后方存在一定空间用于显示对错
        Options = Data["options"]        
        answerNum = Data["answer_num"]#答案数量
        Selections = 0 
        X = 35 
        Y = 430
        lenselections = len(Options)
        while  (Selections < lenselections):
            if Options[Selections]["answer"] == True :
                pyautogui.click(x=X, y=Y, clicks=1, button='left')
                print   (Options[Selections]["content"])

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

        pyautogui.click(x=450, y=1000, clicks=1, button='left')


    elif AnswerTypeMultiCombine == True:
        #连接词组题
        selectnums = Data["stem"]
        content = selectnums["content"]
        #拿到一共需要选几个
        contentlen = len(content)
        answerContent = Data["answer_content"]
        answer = answerContent["answer_arr"]
        Options = Data["options"]
        lengans = len(answer)
        roll1 = 0
        roll2 = 0
        lenoption = len(Options)
        while (roll2 < lengans):
            if answer[roll2] == Options[roll1]["content"] :
                click = roll1 + 1
                if click % 2 == 1 :
                    X = 150 
                else:
                    X = 350
                Y = ( roll1 // 2 ) * 70 + 500
                pyautogui.click(x=X, y=Y, clicks=1, button='left')
                roll2 = roll2 + 1
                roll1 = 0
            else:
                roll1 = roll1 + 1
        pyautogui.click(x=450, y=1000, clicks=1, button='left')
        


    roll = roll + 1
    openfile.close()