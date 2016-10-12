# -*- coding: utf-8 -*-
from miette import DocReader as docs

import re
def pars_doc(url, file=""):
    
    #url=u"C:\\Users\\user\\Google Диск\\Доступы\\Терминалы\\Владикавказ_rub90 Терминалы зал Мамсурова-Реал.doc"
    string=url+file
    doc=docs(string)
    list=doc.read(10000)#.split("\n")
    #print(list)
    pat_name="T-[0-9]+"
    pat_key="\d{6}-\d{6}-\d{6}-\d{6}-\d{6}-\d{6}"
    pat_part="(?<=Партнерская группа:)[A-я \w-]+"
    pat_club="(?<=Клуб:)[A-я \w-]+"
    pat_admin="(?<=Логин:)([A-z \w-]*)"
    pat_pas="(?<=Пароль:)([A-z \w-]*)"
    name_list=re.findall(pat_name,list)
    key_list=re.findall(pat_key,list)
    part_list=re.findall(pat_part,list)
    club_list=re.findall(pat_club,list)
    admin_list=re.findall(pat_admin,list)
    pas_list=re.findall(pat_pas,list)
    #print(pas_list)
    if len(admin_list)==0:
        admin=""
    else:
        admin=admin_list[0].decode("utf-8").replace(" ","")
    if len(pas_list)==0:
        pas=""
    else:
        pas=pas_list[0].decode("utf-8").replace(" ","")
    
    part=part_list[0].decode("utf-8").strip()
    club=club_list[0].decode("utf-8").strip()
    #print(part)
    lo=[]
    for i in xrange(len(name_list)):
        lo.append({"club":club,"pas":pas,"name":name_list[i], "key":key_list[i],"part":part, "admin":admin})
    return lo

#print(pars_doc("22"))
