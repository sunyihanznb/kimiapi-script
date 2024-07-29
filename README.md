# kimiapi-script
一个基于python的kimi/openai的api调用脚本,自带指令设置和连续对话记忆

## 如何使用
### 使用release:
直接双击程序运行即可

### 使用gitclone
在终端中输入
```
gitclone https://github.com/sunyihanznb/kimiapi-script.git
```
之后双击运行"启动脚本.bat"

## 启动流程
### 1.第一次启动
第一次启动时会要求输入apikey,需要自行前往kimi控制台获取
以上功能位于testapikey.py

### 2.检查依赖
之后会检查依赖,若缺失会自行安装
ps:若安装失败或安装后仍然报错,请输入以下命令:
```
pip install pydantic_core
```
```
pip install openai
```
```
pip install colorama
```
以上功能位于testlib.py

### 3.使用
控制台提示键入便可输入问题
以上功能位于main.py

## 命令
### /help
输入/help可以查看命令列表和命令用途

### /stop
用于停止控制台

### /prompt
输入后可以更改kimi的提示词

### /memory_setting
更改记忆次数(多少次对话后会清除记忆以节省token)

### /tips
用于开关"/help"提示

### /file
可以给kimi上传文件并跟随一次对话,输入命令后需要输入文件路径
kimi官方给文件功能的介绍是:
"我们支持文本文件和图片文件，对于图片文件，我们提供了 OCR 的能力"

### /rpm
设置rpm数(rpm:一分钟内可以发送消息的次数,超过会报错),达到限度自动暂停

### /model
设置模型,可以在列表中选择,数字越大越适合长文本生成

以上指令功能位于main.py
