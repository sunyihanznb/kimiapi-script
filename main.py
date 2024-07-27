import testlib
import TestApiKey
import os
import time
import updatefile
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

testlib.testlib()
from openai import OpenAI

if os.path.isfile("key.txt") == False:
    TestApiKey.Creat_File()

api_key = TestApiKey.Read_File()

client = OpenAI(
    api_key = api_key,
    base_url = "https://api.moonshot.cn/v1",
)

prompt = "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"

messages = [
	{"role": "system", "content": prompt},
]

messages2 = []

memory_setting = 10

def chat(input):
    """
	chat 函数支持多轮对话，每次调用 chat 函数与 Kimi 大模型对话时，Kimi 大模型都会”看到“此前已经
	产生的历史对话消息，换句话说，Kimi 大模型拥有了记忆。
	"""
 
	# 我们将用户最新的问题构造成一个 message（role=user），并添加到 messages 的尾部
    messages.append({
		"role": "user",
		"content": input,	
	})

    # 携带 messages 与 Kimi 大模型对话
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=messages,
        temperature=0.3,
    )

    # 通过 API 我们获得了 Kimi 大模型给予我们的回复消息（role=assistant）
    assistant_message = completion.choices[0].message

    # 为了让 Kimi 大模型拥有完整的记忆，我们必须将 Kimi 大模型返回给我们的消息也添加到 messages 中
    messages.append(assistant_message)

    return assistant_message.content

tips = True

while True:
    if tips == True:
        print(Fore.YELLOW + "查看自带指令请输入" + Fore.BLUE + "/help")
    input_message = input("键入提问:")
    if input_message == "/help":
        print(Fore.GREEN + "/stop 结束对话\n/file 上传文件\n/prompt 更改提示词\n/memory_setting 更改记忆次数\n/tips 开关'/help'提示")
    elif input_message == "/stop":
        break
    elif input_message== "/prompt":
        print(Fore.YELLOW + "当前提示词:" + prompt)
        prompt = input("请输入新提示词:")
        print(Fore.GREEN + "更改完成!")
    elif input_message == "/memory_setting":
        print(Fore.YELLOW + "当前记忆次数:" + memory_setting)
        memory_setting = input("输入新的记忆次数:")
        print(Fore.GREEN + "更改完成!")
    elif input_message == "/tips":
        print(Fore.YELLOW + "当前tips设置:" + str(tips))
        change_tips = input("确定更改?(y/n)")
        if change_tips == "y":
            if tips == True:
                tips = False
            else:
                tips = True
            print(Fore.GREEN + "更改完成!")
            print(Fore.YELLOW + "当前tips设置:" + str(tips))
        else:
            print(Fore.YELLOW + "设置未更改")
    else:
        if input_message == "/file":
            #print("文件处理暂不可用!")
            file_path = input("输入文件路径:")
            messages = updatefile.updatefile(file_path,messages,client)
            input_message = input("键入提问,将与文件一同发送:")
        print(chat(str(input_message)))
        print(Fore.YELLOW + "处理中...")
        time.sleep(5)

        memory_number = len(messages) - 1
        print("本次对话记忆数:" + str(memory_number))
        if memory_number >= int(memory_setting):
            messages2 = messages[0]
            messages = messages.clear
            messages = messages2
            messages2 = messages2.clear
            print(Fore.YELLOW + "达到最大限度,自动清除记忆")
