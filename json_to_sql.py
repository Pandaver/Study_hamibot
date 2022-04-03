#-*- coding: UTF-8 -*-
import json
import re
import time

with open('H:\QuestionBank.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    for key, value in json_data.items():
        pie = re.split(r"[\|]", key)
#            sort = {'1': }
        if value == pie[1] :
            options = 'A'
        elif value == pie[2] :
            options = 'B'
        elif value == pie[3] :
            options = 'C'
        elif value == pie[4] :
            options = 'D'
        else:
            options = 'NULL'
        str = 'INSERT INTO "tiku" VALUES (' + "'" + key + "'" + ',' + "'" + value + "'" + ", NULL, '" + options + "', '" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) +"');"
# 睿智
#        print(str)
        f = open('H:\QuestionBank.sql','a',encoding='utf8')
        f.write('\n' + str)
        f.close()
