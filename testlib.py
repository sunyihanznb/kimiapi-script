import os
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

def testlib():
    print("检测支持库是否存在...")
    try:
        import openai
        import colorama
    except ModuleNotFoundError:
        while True:
            reply = input(Fore.RED + "检测到缺失,是否安装?(y/n)")
            if reply == y:
                print("正在安装...")
                os.system("pip install pydantic_core")
                os.system("pip install openai")
                os.system("pip install colorama")
                print("安装完成")
                break
            elif reply == n:
                print(Fore.YELLOW + "程序即将推出")
                break
            else:
                return
    finally:
        print(Fore.GREEN + "检查完成")
