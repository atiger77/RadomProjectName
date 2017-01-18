#coding: utf-8
'''
Author:
       __  _             ________
 ___ _/ /_(_)__ ____ ___/_  /_  /
/ _ `/ __/ / _ `/ -_) __// / / / 
\_,_/\__/_/\_, /\__/_/  /_/ /_/  
          /___/   

Date:20170117
Desc:执行后脚本默认会随机返回一个项目名称（英文&中文），名字是从字典文件中读取，目前字典有希腊神话，dota英雄名字，漫威人物姓名和行星名字。
Version:1.0

'''
import random,re

def RandomProjectName():
    D,G,M,P = "DOTA_Hero.txt","Greek_mythology.txt","Marvel_Comics.txt","Planet_name.txt"
    dict_pwd = "dict/"     
    dict_file_pwd = dict_pwd + D
    sum_en_list = []

    with open (dict_file_pwd,'r') as f:
        a = f.readlines()
        for i in a:
            b = i.split()
            sum_en_list.append(b[0])
    name_random =  random.choice(sum_en_list)

    with open (dict_file_pwd,'r') as fi:
        z = fi.readlines()
        for i in z:
            b = i.split()
            if name_random in b:
                print b[0],b[1]
                break

if __name__ == '__main__':
    try:
        RandomProjectName()
    except Exception,e:
        print e   
