
#读取并保存为csv格式文件。遍历全院300多位老师主页，存储300多位老师的基本信息。
import requests
from lxml import etree
import re
import csv


dataurl = []


headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "JSESSIONID=EAA82442117D7E2B6FEEC1404E244C3D; UqZBpD3n3iPIDwJU=v1K6FbQwSDYkW",
        "Host": "faculty.xidian.edu.cn",
        "Origin": "https://faculty.xidian.edu.cn",
        "Referer": "https://faculty.xidian.edu.cn/xyjslb.jsp?totalpage=16&PAGENUM=2&urltype=tsites.CollegeTeacherList&wbtreeid=1001&st=0&id=1583&lang=zh_CN",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50",
        "X-Requested-With": "XMLHttpRequest",
    }


def geturl():  
    url = "https://faculty.xidian.edu.cn/xyjslb.jsp"
    parms = {
    "totalpage" : "16",
    "PAGENUM" : 1,
    "urltype" : "tsites.CollegeTeacherList",
    "wbtreeid" : "1001",
    "st":"0",
    "id":"1583",
    "lang":"zh_CN",
    }   
    n = 1
    for i in range(1,17):
        parms["PAGENUM"] = i
        resp = requests.get(url=url,headers=headers,params=parms)
        tree = etree.HTML(resp.text)
        result = tree.xpath("/html/body/div[5]/div/div/div[3]/ul/li")
        for i in result:
            teaurl=i.xpath('./a/@href')
            dataurl.append(teaurl)
        print("已完成第{}页".format(n))
        n+=1


def getdata(url):
    resp = requests.get(url[0])
    resp.encoding = "utf-8"
    
    result  =  re.finditer(r'class="t_photo".*?<span>(?P<name>.*?)</span>',resp.text,re.S)
    for i in result:
        name = i.group("name").strip()
        save(name)
        

def save(name):
    s = ["姓名","性别","毕业院校","学历","学位","单位","院系","学科"]
    header = [name]
    with open('result.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)


def main():
    geturl()
    for i in dataurl:
        getdata(i)


if __name__ == "__main__":
    main()