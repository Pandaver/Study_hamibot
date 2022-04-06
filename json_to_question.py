#-*- coding: UTF-8 -*-
import json
import re
import time

i = 0
with open('H:\Study_hamibot\QuestionBank.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)
    for key, value in json_data.items():
        pie = re.split(r"[\|]", key)
#        print(pie)
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
        if len(pie) == 3:
            strt = options + " " + pie[0] + " " + pie[1] + "	" + pie[2]
        elif len(pie) == 4:
            strt = options + " " + pie[0] + " " + pie[1] + "	" + pie[2] + "	" + pie[3]
        elif len(pie) == 5:
            strt = options + " " + pie[0] + " " + pie[1] + "	" + pie[2] + "	" + pie[3] + "	" + pie[4]
#            strt = 'INSERT INTO "tiku" VALUES (' + "'" + pie[0]+pie[1]+'、'+pie[2] + "'" + ',' + "'" + value + "'" + ", NULL, '" + options + "', '" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) +"');"
#        if (pie[4] == )
#        strt = options + " " + pie[0] + " " + pie[1] + "	"
        f = open('H:\Study_hamibot\question','a',encoding='utf8')
        f.write(strt + "\n")
        f.close()
        i = i + 1
        stri=str(i)
        print("已处理" +stri + "条数据")
# 睿智
