# 学习永远是自己的事情
###### 我寻思着我因为懒才写这玩意的 ，整的现在每天更新脚本，咋还变勤快了呢...来看的都是懒狗🐶🐶🐶🐶🐶🐶🐶🐶🐶 
##### 这位同学，用我源码就用了...我这GPL 3.0 协议就是给二次开发看的 ， 加上我名字这么难吗?
![logo](https://s1.ax1x.com/2020/04/08/GRyPCq.png "logo")
# Word-Master-α
Alpha，是第1个希腊字母。「Alpha」常用作形容词，以显示某件事物中最重要或最初的，例如软体工程中的Alpha版本。 --wikipedia
##### 所以由于一些原因,现在不能达到100%自动满分.以后的版本亦不能保证.
# 食用方法
# [视频强烈推荐看一下](https://b23.tv/BV1Vz41187T9 "release")
视频里面少说一点东西，有问题问我，先不重录视频了(重录视频肯定把这句话删掉 4.16
1. 从我们的[release](../../releases "release")界面下载最新的版本，解压

2. 打开`Fiddler/Fiddler.exe`

3. 按照视频设置过滤器和FiddlerScript,在FiddlerScript的OnResponse里加入
```
if(oSession.uriContains("https://wap.vocabgo.com/Student/ClassTask")){
    oSession.utilDecodeResponse();//解码数据包
    oSession.SaveResponse("../ThisDataPacket.txt",true);//储存数据包
    oSession.SaveResponseBody("../ThisDataPacketBody.json");
}
```

3. 打开电脑端词达人，并位于第一题(我并没有写认识单词的界面，所以你需要手动跳过)

4. 把窗口位于最左，并且高度全满，宽度最小（如图，**而且目前只支持1920 x 1080 分辨率的输出**）

5. power shell打开Main.exe 自动完成。

1. **附加:1.3 版本新增了user.json选项 以后允许用户对脚本进行更多的自定义项目**
```
{
    "rolltime":300
}
```
# 注意事项
-   由于 alpha 版存在bug，所以我引入了自动暂停机制，其次所有正确答案输出在屏幕上，便于手动点击。

# 效率
![](https://s1.ax1x.com/2020/04/08/GRfEWj.png)
脚本运行时间2min23s，正确率98.62%
![](https://s1.ax1x.com/2020/04/13/GjrGgP.png)
1.3版本的效率(由于我用的是热点 ，延迟大 好几次都是词达人服务器拉跨，所以你们应该还会快一点)
#### 2020.4.13补充: 新版（1.3）的效率较于1.2 已经大幅度提升 欢迎更新233
#### 2020.4.12补充:因为词达人官方同学进行干扰，这种秒速在这个版本(V1.2)是见不到了QAQ...也许未来还会再见

# 时间轴
###### 4.16 前几天一个同学跟我聊天，说他是直接伪造请求。我觉着挺好，但是我这种懒狗...唉，可能不会去分析请求，有这时间还不如跟**女孩子**聊天呢QAQ
###### 复现了 3 - 4次110003错误 ， 下个版本看看能不能规避
###### 4.13 word master 1.3 版更新，简化了代码复杂度 利用函数编程降低整体耦合度 易于维护和升级
###### 下个版本想加点自定义项目,然后改一下代码精度，减小一点逻辑复杂度 : )
###### 4.12 感谢vocabgo 官方 ，因为开始堵脚本，不但绕过了，还修复了几个bug2333333，等会更新

# 编译 & 二次开发
**使用GPL协议,如果要用代码的话建议先去看看什么是[GPL协议](https://www.gnu.org/licenses/gpl-3.0.html "GPL协议")**
-  环境配置
我们的release 版本均采用 Win10 64 bit 环境配置，32bit理论通用，由于加载库的原因，目前尚未支持Linux以及mac os。安装最新的python3 及 pip
- 执行`pip install pyautogui`安装依赖库
- 用你的IDE打开并修改,编译
# Credits
[pyautogui](https://github.com/asweigart/pyautogui "pyautogui")
# LICENSE
[GPL V3.0](LICENSE "GPL V3.0")
