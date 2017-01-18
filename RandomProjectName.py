#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   

Date:20170118
Desc:执行后脚本默认会随机返回一个项目名称（英文&中文），名字是从字典文件中读取，目前字典有希腊神话，dota英雄名字，漫威人物姓名和行星名字。
Version:2.0

'''
import random,sys
from optparse import OptionParser

def RandomProjectName(argv):
    dict_name = {"D":"DOTA_Hero.txt","G":"Greek_mythology.txt","M":"Marvel_Comics.txt","P":"Planet_name.txt"}
    dict_pwd = "dict/"     
    dict_file_pwd = dict_pwd + dict_name[argv]
    sum_list = []

    with open (dict_file_pwd,'r') as f:
        file_readline = f.readlines()
        line_num = len(file_readline)
        random_line = random.randrange(1,line_num+1)
        #print random_line
        line_count =0
        for i in file_readline:
            b = i.split()
            sum_list.append(i)
            for j in sum_list:
                line_count +=1
                if (line_count == random_line):
                    print j,

def Example():
    print '''usage: python RandomProjectName.py [dict name]
example: 
$ python RandomProjectName.py G
$ Zeus 天神宙斯

DictNameList:
D:DOTA_Hero.txt   
G:Greek_mythology.txt
M:Marvel_Comics.txt
P:Planet_name.txt'''

if __name__ == '__main__':
    if len(sys.argv) == 1:
        RandomProjectName("D")
    elif len(sys.argv) == 2:
        choice = ["D","G","M","P"]
        if sys.argv[1] in choice: 
            RandomProjectName(sys.argv[1])
        else:
            Example()
    else:
        Example()
