from pathlib import Path
from openai import OpenAI
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

def updatefile(file_path,messages,client):
    # moonshot.pdf 是一个示例文件, 我们支持文本文件和图片文件，对于图片文件，我们提供了 OCR 的能力
    # 上传文件时，我们可以直接使用 openai 库的文件上传 API，使用标准库 pathlib 中的 Path 构造文件
    # 对象，并将其传入 file 参数即可，同时将 purpose 参数设置为 file-extract；注意，目前文件上传
    # 接口仅支持 file-extract 一种 purpose 值。
    file_object = client.files.create(file=Path(file_path), purpose="file-extract")
    
    # 获取结果
    # file_content = client.files.retrieve_content(file_id=file_object.id)
    # 注意，某些旧版本示例中的 retrieve_content API 在最新版本标记了 warning, 可以用下面这行代替
    # （如果使用旧版本的 SDK，可以继续延用 retrieve_content API）
    file_content = client.files.content(file_id=file_object.id).text

    try:
        messages.append({"role": "system", "content": file_content})
    except:
        print(Fore.RED + "需传入字典")
    return messages