# 您猜怎么着，👴英语结课了。暑假再说
![logo](https://s1.ax1x.com/2020/04/08/GRyPCq.png "logo")
# Word-Master-β
在电脑范畴，Beta软件也能代表电脑软件的测试版，通常指的是公开测试版，提供一般使用者协助测试并回报问题。详见软件出版周期。 -β 版本
# 食用方法
# [视频](https://b23.tv/BV1Vz41187T9 "release")

1. **附加:1.3 版本新增了user.json选项 以后允许用户对脚本进行更多的自定义项目**
```
{
    "waitTime":"0.5",
    "NightMode":"0",
    "autoMode":{
        "fillchart":"1",
        "singleSelect":"1",
        "combine":"1",
        "multiselect":"1"
    }
}
```
waittime：点击默认延迟，规避错误
automode：0:只显示答案 ，1：做题
nightmode：全自动答题
# 注意事项
-   由于 beta 版也可能存在bug，所以我引入了自动暂停机制，其次所有正确答案输出在屏幕上，便于手动点击。

# 效率
![JyqwxP.png](https://s1.ax1x.com/2020/04/25/JyqwxP.png)
2.1beta 效率
![](https://s1.ax1x.com/2020/04/23/JwLwL9.png)
2.0beta效率
![](https://s1.ax1x.com/2020/04/08/GRfEWj.png)
脚本运行时间2min23s，正确率98.62%
![](https://s1.ax1x.com/2020/04/13/GjrGgP.png)
1.3版本的效率(由于我用的是热点 ，延迟大 好几次都是词达人服务器拉跨，所以你们应该还会快一点)
#### 2020.4.13补充: 新版（1.3）的效率较于1.2 已经大幅度提升 欢迎更新233
#### 2020.4.12补充:因为词达人官方同学进行干扰，这种秒速在这个版本(V1.2)是见不到了QAQ...也许未来还会再见

# 时间轴
###### 4.25 2.1beta
2.1: 
2020.4.25
simpified code and logic
fillchart : add copy
optimize voice question logic and judgement ,speed up the effenction
added new autoMode and print mode for just print the ans 
no rolltime any longer
fix can not auto stop bug
fix some annoying bug

###### 4.23 New version (beta) realeased
###### 4.16 前几天一个同学跟我聊天，说他是直接伪造请求。我觉着挺好，但是我这种懒狗...唉，可能不会去分析请求
###### 复现了 3 - 4次110003错误 ， 下个版本看看能不能规避
###### 4.13 word master 1.3 版更新，简化了代码复杂度 利用函数编程降低整体耦合度 易于维护和升级
###### 下个版本想加点自定义项目,然后改一下代码精度，减小一点逻辑复杂度 : )
###### 4.12 感谢vocabgo 官方 ，因为开始堵脚本，不但绕过了，还修复了几个bug2333333，等会更新

# 编译 & 二次开发
**使用GPL协议,如果要用代码的话建议先去看看什么是[GPL协议](https://www.gnu.org/licenses/gpl-3.0.html "GPL协议")**
[GPL协议官方中文版](https://jxself.org/translations/gpl-3.zh.shtml "GPL协议")
-  环境配置
我们的release 版本均采用 Win10 64 bit 环境配置，32bit理论通用，由于加载库的原因，目前尚未支持Linux以及mac os。安装最新的python3 及 pip
- 执行
```
安装依赖库
pip install pyautogui
pip install pytesseract

```
- 用你的IDE打开并修改,编译
# Credits
[pyautogui](https://github.com/asweigart/pyautogui "pyautogui")
[pytesseract](https://github.com/madmaze/pytesseract "pytesseract")
[keyboard](https://github.com/boppreh/keyboard "keyboard")
[PIL](https://github.com/python-pillow/Pillow "pillow")

# LICENSE
[GPL V3.0](LICENSE "GPL V3.0")
