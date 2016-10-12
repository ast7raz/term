#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import glob
import time
from doc import pars_doc
from dbproof import save

#Функция ищет все файлы с именем filename во всех подкаталогах каталога catalog

def find_files(catalog):
    files=[]
    catalog=catalog.decode("utf-8")
    names=glob.glob(catalog)
    for name in names:
        if os.path.isfile(name):
            files.append(name)
    return files
while True:
    #print("test")
    key_list=[]
    f=open("list.txt","r")
    files=find_files("C:\\Users\\user\\Google Диск\\Доступы\\Терминалы\\*.doc")
    #print(files)
    aux=[line.strip().decode("utf-8") for line in f]
    f.close()
    #print(len(aux))
    #print(aux)
    #print(len(files))
    files= [e for e in files if not e in aux]
    #print(files)
    if len(files)!=0: 
        f=open("list.txt","w")
        for file1 in files:
            #print(file1)
            try:
                keys=pars_doc(file1)
                for key in keys:
                    key_list.append(key)
                aux.append(file1.encode("utf-8"))
            except:
                print(file1)
        try:
            f.write("\n".join(aux))
            f.close()
        except UnicodeError:
            print(u"Не был записан файл со списком обработтаных файлов из за ошибки")
            f.close()
    for key in key_list:
        
        save(key)
    time.sleep(30)
