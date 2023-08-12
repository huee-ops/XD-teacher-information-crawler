# 记录一下神奇的代码编写环节：
#     首先我准备使用电脑对西电教师主页进行爬取
#     然后步骤分解了得到每个老师的网址
#     然后解析每个老师网址
#     结果错误百出，解析经常出现问题
#     然后我就一不小心点了手机的UI
#     发现反馈的包中包括了所有的老师地址
#     只需要解析那个json文件就可以了
#     然后csv保存

import requests
from lxml import etree
import csv

with open('result.csv', 'w+', encoding='utf-8', newline='') as f:
    s = ["姓名","职称","性别","毕业院校","学历","学位","单位","学科","邮箱","联系方式","位置","点击数"]
    writer = csv.writer(f)
    writer.writerow(s)
f.close()
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Cookie": "JSESSIONID=0E9F54468974A09E8DDA378DF18A1AF9; UqZBpD3n3iPIDwJU=v1K6FbQwSDYkW",
    "Host": "faculty.xidian.edu.cn",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.56",
    "X-Requested-With": "XMLHttpRequest",
}
# def getsid():
#     pass
# def gethomeid(): 放弃了这个步骤，换用每次请求url根据lxml查询获得
#     pass

def getclick(url):
    headers = {
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "Sec-Fetch-Dest": "empty",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36 Edg/110.0.1587.69",
    }
    respp = requests.get(url,headers=headers)
    pass

    
def getdata():
    num = 0
    n = 0
    for k in range(0,400,6):
        url = "https://faculty.xidian.edu.cn/system/resource/tsites/getsitelistcontent.jsp?collegeId=1583&disciplineId=0&honorId=0&pinYin=&requestUrl=http%3A%2F%2Ffaculty.xidian.edu.cn%2Fxyjslb.m.jsp&comType=collegeTeacher&treeid=1001&lang=zh_CN&viewmode=8&viewid=70564&siteOwner=1438110714&start={a}&end={b}&startnum={a}&endnum={b}&viewUniqueId=u7".format(a=k,b=k+6)
        resp = requests.get(url=url,headers=headers)
        result = resp.json()
        w = 0
        for i in result:            
            n+=1
            w+=1
            #将教师的 姓名，职称，性别，毕业院校，学历，学位，单位，院系，点击次数等信息  
            name = i["name"]
            prorank = i["prorank"]
            sex = i["sex"]
            graduatedUniversity = i["graduatedUniversity"]
            education = i["education"]
            degree = i["degree"]
            unit = i["unit"]
            email = i["email"]
            discipline = i["discipline"]
            contact = i["contact"]
            officeLocation = i["officeLocation"]
            url = i["url"]
            num+=1
            a = [name,prorank,sex,graduatedUniversity,education,degree,unit,discipline,email,contact,officeLocation,url]
            # print("正在打印",n)
        
            save(a)
        print("------------------------------",w,k)

def save(a):
    s = ["姓名","职称","性别","毕业院校","学历","学位","单位","学科","邮箱","联系方式","位置","网址"]
    with open('result.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(a)
    f.close()

def main():
    getdata()

if __name__ == "__main__":
    main()