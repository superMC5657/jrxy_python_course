## 课程要求

本课程的课程内容在[README](README.md)上可以读到，有任何问题或者建议，请联系授课老师。

本课程需要你对以下内容具有初步的了解，由于课堂时间有限，因此希望你能通过课余的时间进行查漏补缺。

1. Anaconda 

    [Anaconda](https://www.anaconda.com)指的是一个开源的Python发行版本，其包含了Python, R等180多个科学包及其依赖项。这是什么意思呢？Python是一门编程语言，使用这门语言的时候，在写代码这件事情之外，还有很多其他的配套工作，比如运行脚本、下载各种需要用到的库、管理环境等。Anaconda就把这些功能全都集成好了，省去很多琐碎的工作。简单来说，Anaconda帮你管理了在使用Python时用到的包和环境。
    
    Anaconda集成了大部分需要用到的Python包，尤其是数据科学类的包，在数据处理方面，你几乎可以在安装后直接进行使用。
    
    利用自带的conda，Anaconda能够对Python包安装、卸载和更新。Python的一大优势即是丰富的第三方的包，比如数据处理的numpy、数据分析的pandas、和我们做深度学习用到的keras，都是我们所说的包。安装和管理这些包是使用Python的日常。Anaconda是一个便利简洁的包管理器。
    
    **下载使用：**
    
    如果你嫌官网下载太慢,这里建议大家使用[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)，找到对应的anaconda版本和操作系统即可。
    
    >注意：建议大家下载稳定版本，最新版本可能存在BUG，Anaconda3-5.3.1版本就比较稳定。

    下载后按提示安装就可以了。

    安装完Anaconda，就相当于安装了Python、命令行工具Anadonda Prompt、集成开发环境Spyder、交互式笔记本IPython和Jupyter Notebook。


2. Github

    Git是什么？

    Git是目前世界上最先进的**分布式版本控制系统**（没有之一）。分布式相比于集中式的最大区别在于开发者可以提交到本地，每个开发者通过克隆（git clone），在本地机器上拷贝一个完整的Git仓库。

    那什么是版本控制系统？ 
    
    如果你用Microsoft Word写过长篇大论，那你一定有这样的经历：

    想删除一个段落，又怕将来想恢复找不回来怎么办？有办法，先把当前文件“另存为……”一个新的Word文件，再接着改，改到一定程度，再“另存为……”一个新文件，这样一直改下去，最后你的Word文档变成了这样：
    ![图片](0.jfif)
    
    过了一周，你想找回被删除的文字，但是已经记不清删除前保存在哪个文件里了，只好一个一个文件去找；看着一堆乱七八糟的文件，想保留最新的一个，然后把其他的删掉，又怕哪天会用上，还不敢删。

    如果有些部分需要你的同学帮助填写，于是你把文件Copy到U盘里给她（也可能通过Email发送一份给她），然后，你继续修改Word文件。一天后，同事再把Word文件传给你，此时，你必须想想，发给她之后到你收到她的文件期间，你作了哪些改动，得把你的改动和她的部分合并。

    如果有一个软件，不但能自动帮我记录每次文件的改动，还可以让同事协作编辑，这样就不用自己管理一堆类似的文件了，也不需要把文件传来传去。如果想查看某次改动，只需要在软件里瞄一眼就可以，岂不是很方便？

    这个软件用起来就应该像这个样子，能记录每次文件的改动：
    
    |  版本  | 文件名 | 用户 | 说明 | 日期 |
    |  ----  | ----  | ---- | ---- | ---- |
    | 1  | document.doc | 张三 | 增加了XX内容 | 2021.06.20 16:00 |
    | 2  | document.doc | 李四 | 更改了xx格式 | 2021.07.03 17:43|
    | 3  | …… | …… | …… | …… |
    
    Git就能帮助你实现这样的功能。
    
    Github (Git远程仓库)
    >如果你是一枚Coder，但是你不知道Github，那么我觉的你就不是一个菜鸟级别的Coder，因为你压根不是真正Coder，你只是一个Code搬运工。
    
    什么是 Github?
    
    Git是一个分布式版本控制系统，简单的说其就是一个软件，用于记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的软件。
    
    Github([官网地址](www.github.com))是一个基于git的代码托管平台（当然可以放的不只是代码），付费用户可以建私人仓库，我们一般的免费用户只能使用公共仓库，也就是代码要公开。
    
    今天，GitHub已是这个星球上最流行的开源托管服务。目前已托管几百万的git项目，不仅越来越多知名开源项目迁入GitHub，近三年流行的开源库往往在GitHub首发。
    
    **注册账户以及创建仓库：**
    要想使用github第一步当然是注册github账号了， 在其[官网](https://github.com/)进行注册。 之后就可以创建仓库了（免费用户只能建公共仓库），Create a New Repository，填好名称后Create，之后会出现一些仓库的配置信息。
    
    推荐在本课程中使用**Github Desktop**，具体内容可参见其[官网地址](https://desktop.github.com/)。 并可以在官网下载适合你的版本。
    
    下载：百度云盘(链接：https://pan.baidu.com/s/1UBez48hB0FEXDEOMMsaJqw 密码：6fkr)
    
    下面提供一个友好的帮助文档，可以帮助你一步一步注册Github，并安装Desktop，你可以很方便的将你想要的内容从别人的代码仓库里面clone出来，也可以迅速上传你的代码给别人分享。
    
    [GitHub Desktop图文教程](https://www.jianshu.com/p/a6fc842f501d)
    
3. Markdown

    **Markdown**是一种轻量级标记语言。 它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML（或者HTML）文档。这种语言吸收了很多在电子邮件中已有的纯文本标记的特性。由于Markdown的轻量化、易读易写特性，并且对于**图片，图表、数学式**都有支持，目前许多网站都广泛使用Markdown来撰写帮助文档或是用于论坛上发表消息。Markdown 编写的文档可以导出 HTML、Word、图像、PDF、Epub等多种格式的文档。Markdown 编写的文档后缀为 .md或.markdown。
    
    **编辑器**：推荐使用[Typora](https://typora.io/)（[一个极简教程](https://zhuanlan.zhihu.com/p/148825412)），它适用于Windows或者MacOS操作系统。如果你使用印象笔记，有道云笔记，发布微信公众号等都用的上。
    
    当然你也可以使用**JupyterLab**生成.md文件并进行编辑。
    
    给大家几个有效的链接：
    - Markdown指南中文版 [访问](https://www.markdown.xyz/)
    - Markdown 入门指南 [访问](https://www.jianshu.com/p/1e402922ee32)
    - 各种不同的编辑器 [访问](https://zhuanlan.zhihu.com/p/69210764)


4. JupyterNotebook or JupyterLab

    Jupyter Notebook是基于网页的用于交互计算的应用程序。其可被应用于全过程计算：开发、文档编写、运行代码和展示结果。——[Jupyter Notebook官方介绍](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)
    
    简而言之，Jupyter Notebook是以网页的形式打开，可以在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示。如在编程过程中需要编写说明文档，可在同一个页面中直接编写，便于作及时的说明和解释。

    Jupyter Notebook中所有交互计算、编写说明文档、数学公式、图片以及其他富媒体形式的输入和输出，都是以文档的形式体现的。这些文档是保存为后缀名为.ipynb的JSON格式文件，不仅便于版本控制，也方便与他人共享。此外，文档还可以导出为：HTML、LaTeX、PDF等格式。
    
    >好消息：在你安装了Anaconda之后，事实上Jupyter Notebook已经被集成了。

    **本课程的所有教案，都是通过Jupyter Notebook撰写的。**

    **Jupyter Lab**是一个交互式的开发环境，是Jupyter Notebook的下一代产品，集成了更多的功能。对于Jupyter Notebook有着完全的支持。
    
    通过使用JupyterLab，能够以灵活，集成和可扩展的方式处理文档和活动：

    - 可以开启终端，用于交互式运行代码，完全支持丰富的输出
    - 支持Markdown，Python，R，LaTeX等任何文本文件
    - 增强notebook功能
    - 更多插件支持
    
    JupyterLab 目前的版本是1.0版本，如果你安装的是早先的Anaconda，你的JupyterLab版本可能过早，建议你可以使用 pip install jupyterlab --upgrade 来完成升级。


### 个人推荐

以下的内容是我个人的推荐，相信对你的学习会有用的。

1. Notebook（笔记软件）

    印象笔记Evernote的移动端体验是我用过各种笔记软件中最好的，优秀的功能排版，贴心的快捷输入，还有提醒、待办等等功能。剪藏功能非常棒，用来收集资料，整理思路再好不过了。
    
    [下载链接](https://www.yinxiang.com/download/)
     
     
2. Xmind（绘制漂亮的思维导图）

    XMind 是一个全功能的思维导图和头脑风暴软件，它能与用户其它的Office软件紧密集成。此外，XMind也支持导入用户的MindManager和FreeMind文件。作好的思维导图也可以保存到Evernote并在移动端查看。
    
    相关教程：  
    - XMind使用教程入门 [链接](https://zhuanlan.zhihu.com/p/47772905)  
    - 思维导图神器Xmind使用指南 [链接](https://zhuanlan.zhihu.com/p/32048362)  

    [下载链接](https://www.xmind.cn/download/)

3. Mendeley（参考文献的整理利器）

    Mendeley主要功能：
    - 参考文献管理
    - PDF文件阅读与标注
    - 自动生成参考文献
  
    优点：
    对文献进行分类，统一管理，文章及其内容搜索功能强大；方便文献阅读，标记、笔记功能齐全，界面简洁养眼；撰写文章时可直接引用Mendeley内添加的文献，并统一进行文献格式修改。  

    相关教程：  
    - Mendeley－一款免费好用的文献管理软件 [链接](https://zhuanlan.zhihu.com/p/28762628)
    - 文献插入引用（Mendeley）+图示说明+完全上手+免费[链接](https://www.jianshu.com/p/cadf09e84c2e)
    
    [下载地址](https://www.mendeley.com/) 


#### 常用网站

代码上有什么不会的地方，或者在策略上希望得到一些启示：

1. 请善于使用搜索引擎。

2. [CSDN](https://www.csdn.net/) 

    CSDN是全球知名中文IT技术交流平台,创建于1999年,包含原创博客、精品问答、职业培训、技术论坛、资源下载等产品服务,提供原创、优质、完整内容的专业IT技术开发社区。

3. [MOOC](https://www.icourse163.org/)

    有很多非常优质的大学课程。

4. [B站](https://www.bilibili.com/) 

    这个大家应该非常熟悉了。


### 机器学习

   机器学习是一门多领域交叉学科，涉及概率论、统计学、凸分析、算法复杂度理论等多门学科。专门研究计算机怎样模拟或实现人类的学习行为，以获取新的知识或技能，重新组织已有的知识结构使之不断改善自身的性能。
    
   它是人工智能的核心，是使计算机具有智能的根本途径。
   1. 机器学习是一门人工智能的科学,该领域的主要研究对象是人工智能，特别是如何在经验学习中改善具体算法的性能。
   2. 机器学习是对能通过经验自动改进的计算机算法的研究。
   3. 机器学习是用数据或以往的经验,以此优化计算机程序的性能标准。
    
   如果你想学习，这里有一些[教材](https://github.com/quantitiveFund/pyQuant/tree/master/Learning/MachineLearning/Reading)。