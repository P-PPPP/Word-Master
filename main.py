# -*- coding: UTF-8 -*-
#copyright ： Peterpei 2020 - 2020 version 2.1 2020.4.25
#be like water
import os.path , time , os , json , pyautogui , pytesseract , random ,pyperclip#规避可能发生的找不到文件问题
from PIL import Image , ImageGrab
lastJson = 0

#读取用户自定设置
scriptpath = os.path.dirname(__file__)
userfilename = os.path.join(scriptpath, 'user.json')
userjson =open(userfilename, encoding = "utf-8", mode="r")

userjson1 = userjson.read()
userJsonDict = json.loads(userjson1)
autoMode = userJsonDict["autoMode"]#是否为自动模式,0为不自动，仅显示 1为自动
nightmode = userJsonDict["NightMode"]#
deftime = userJsonDict["waitTime"]#自定义等待时长
rantime = float(deftime)

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

def fillchart(Data , rantime ,autoMode):#填空题
    answer = Data["answer_content"]
    print   ("正确答案是", answer)
    pyperclip.copy(answer)
    if  int(autoMode["fillchart"]) == 1:
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

def singleSelect(Data , rantime , autoMode):#单选{普通单选 语音单选}
    Options = Data["options"]
    questionDir = Data["stem"]
    question = questionDir["content"]#拿题目长度
    #获取正确选项
    a = 0 #I：正确选项次序
    i = 0  
    while (a < 3):
        if Options[i]["answer"] == True:
            break
        else:
            i = i + 1
            a = a + 1
    print   ("正确答案是",Options[i]["content"])
    if int(autoMode["singleSelect"]) == 1:
        #对题目长度进行分类讨论和适配
        #重写对行数的函数
        length = len(question)
        if 0< length < 20:
            lengy = 1.5
        else:#优化语音题的做题速度和逻辑判断
            position =(0,200,500,800)
            screenshot = ImageGrab.grab(position)
            screenshot.save('test2.PNG', "PNG")#截取题目图片并进行OCR
            file1 = os.path.join(scriptpath, '../test2.PNG')
            ocr = pytesseract.image_to_string(file1)
            line = 0
            null = ""
            while (ocr.splitlines()[line].strip() != null):
                line = line + 1
            lengy = line
            #第一个数值是初始顶端到第一个选项中心的高度 第二个是各选项中心高度差 第三个是描述题目行数高度
            #来源1920 x 1080 的数据.
        ansy = 260 + 70*(i+1) + 45 *(lengy - 1)
        pyautogui.click(x=300, y=ansy, clicks=1, button='left')
        pyautogui.click(x=450, y=1000, clicks=1, button='left')

def multicombine(Data , rantime , autoMode):#链接词组题
    selectnums = Data["stem"]
    content = selectnums["content"]
    contentleng = len(content)
    judgeIfPoints = '..'
    judgeIfPoint = '.'
    if judgeIfPoints in content:
        elements =(contentleng - 1 - 6) / 2 + 1
    elif judgeIfPoint in content:
        elements = (contentleng - 1 - 2)/2 + 1
    else:
        elements = (contentleng - 1) / 2 + 1
    a = 0
    while (a <= 3):
        if a*4 < elements <= (a + 1)*4 :
            length = a 
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
            if int(autoMode["combine"]) == 1:
                pyautogui.click(x=X, y=Y, clicks=1, button='left')
            roll2 = roll2 + 1
            roll1 = 0
        else:
            roll1 = roll1 + 1
    time.sleep(rantime)#停止点击
    if int(autoMode["combine"]) == 1:
        pyautogui.click(x=450, y=1000, clicks=1, button='left')

def multiselectOcr(Data , rantime , autoMode):#新版多选题
    options = Data["options"]
    selections = 0

    position =(0,400,500,900)
    screenshot = ImageGrab.grab(position)
    screenshot.save('test2.PNG', "PNG")#截取题目图片并进行OCR
    file1 = os.path.join(scriptpath, '../test2.PNG')
    ocr = pytesseract.image_to_string(file1)
    line = 0
    realline = 0
    null =""
    print      ("正确答案是:")
    
    while True:
        while (ocr.splitlines()[line].strip() == null):#当行数为空时，自动跳过本行到非空行
            print   ("empty,skipping")
            line = line + 1
        ocrResult =ocr.splitlines()[line].split()#把OCR得到的结果去空，得到纯选项
        item = 0#定义该行第0个OCR结果
        X = 35

        while ( item + 1 <= len(ocrResult) ):#对比答案和选项
            if options[selections]["answer"] == True:
                Y = (realline+1)*75 + 385
                if int(autoMode["multiselect"]) == 1:
                    pyautogui.click(x = X , y = Y)
                print   (options[selections]["content"])
            X = len(ocrResult[item])*18 + 55 + X
            item =item + 1   
            selections = selections + 1

        if len(ocr.splitlines()) <= line + 1 :#当循环到最后一行时退出循环
            break
        line = line + 1
        realline = realline + 1 
    if int(autoMode["multiselect"]) == 1:
        pyautogui.click(x=450, y=1000, clicks=1, button='left')    

def NightMode():
    print   ("Test only")
    while True:
        randX =random.randint(35,400)
        randY =random.randint(400,800)
        pyautogui.click(x =randX , y = randY , button = 'left')
        pyautogui.click(x=450, y=1000, clicks=1, button='left')


#主函数
while True:
    print   ("<<<<<<<<<<<<<")
    start_time = time.time()
    Data = openjsonfile()
#判断题型
    if judgetype(Data)[0] == False:
        fillchart(Data , rantime, autoMode)
        questionStatus = 'fillchart'

    elif judgetype(Data)[0] == True and judgetype(Data)[1] == False and judgetype(Data)[2] == False:
        singleSelect(Data , rantime, autoMode)
        questionStatus = 'singleSelect'

    elif judgetype(Data)[0] == True and judgetype(Data)[1] == True:
        multiselectOcr(Data , rantime, autoMode)
        questionStatus = 'multiselect'

    elif judgetype(Data)[2] == True:
        multicombine(Data, rantime, autoMode)
        questionStatus = 'combine'
#bug反馈机制
    if lastJson == Data :
        bugreport = bugreport + 1
        if autoMode[questionStatus] == 1 and bugreport > 5 and nightmode == 0 :
            break
        elif autoMode[questionStatus] == 0:
            time.sleep(2)
        elif autoMode[questionStatus] == 1 and nightmode == 1:
            NightMode()
    
    else:
        lastJson = Data
        bugreport = 0
#
#    end_time = time.time() - start_time
#    print   ("time spend",end_time)
