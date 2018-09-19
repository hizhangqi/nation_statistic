# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os
print

#http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html

headers = {
    'Host': 'www.stats.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}


start_url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/"


f = open('f:/eee.txt','w')

def visitURL(url,provicenid,json_data_dict,recursion=1):
    # print json_data_dict
    _pid = provicenid
    r = requests.get(url, headers=headers,timeout=10)
    r.encoding = 'gb2312'
    context = BeautifulSoup(r.text, "html.parser")
    sublist =  context.find_all("a")
    i = 1
    sublist1 = []

    for sub in sublist:
        subjson_data = {}
        if u"京ICP备" not in sub.text and i % 2 == 0:
            if u"市辖区" == sub.text or u"县" == sub.text:
                visitURL(start_url + sub.get("href"),_pid,json_data_dict,1)
            elif recursion == 1:
                print  sub.get("href").split("/")[1].replace(".html", "") + "\t" + sub.text + "\t" + _pid
                subjson_data["PROVINCE_ID"] = sub.get("href").split("/")[1].replace(".html", "")
                subjson_data["PROVINCE_NAME"] = sub.text
                sublist1.append(subjson_data)
                json_data_dict['CITIES'] = sublist1
                visitURL(start_url  + sub.get("href"),sub.get("href").split("/")[1].replace(".html",""),subjson_data,0)
            else:
                print "level3:" + sub.get("href").split("/")[1].replace(".html","") + "\t" + sub.text + "\t"+_pid
                subjson_data["PROVINCE_ID"] = sub.get("href").split("/")[1].replace(".html", "")
                subjson_data["PROVINCE_NAME"] = sub.text
                sublist1.append(subjson_data)
                json_data_dict['CITIES'] = sublist1
        i = i + 1
#

r = requests.get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html",headers=headers)
r.encoding='gb2312'
context = BeautifulSoup(r.text,"html.parser")

provincetrs = context.find_all("a")
list = []
for provicetr in provincetrs:
    json_data_dict = {}
    #print provicetr.get("href").replace(".html","")+"\t"+provicetr.text+"\t-1"
    json_data_dict["PROVINCE_ID"] = provicetr.get("href").replace(".html","")
    json_data_dict["PROVINCE_NAME"] = provicetr.text
    visitURL(start_url + provicetr.get("href"),provicetr.get("href").replace(".html",""),json_data_dict)
    list.append(json_data_dict)

for e in list:
    print ' ',e["PROVINCE_NAME"]
    if 'CITIES' in e:
        for sube in e['CITIES']:
            print ' '* 2 ,sube['PROVINCE_NAME']
            if 'CITIES' in sube:
                for t in sube['CITIES']:
                    print ' ' * 3,t["PROVINCE_NAME"]







