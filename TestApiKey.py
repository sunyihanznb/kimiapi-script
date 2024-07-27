import os
import json

def Creat_File():
    file_path = "key.txt"
    key = open(file_path,'w')
    api_key = input("输入密钥:")
    key.write(api_key)
    key.close

def Read_File():
    file_path = "key.txt"
    key = open(file_path,'r')
    return key.read()