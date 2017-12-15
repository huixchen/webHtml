import calendar
import codecs
import datetime
import json

import pymysql
import requests
import time
from bs4 import BeautifulSoup
from dateutil import relativedelta

from com.test.config import *


def get_html(url, data):
    html = requests.get(url, data)
    return html.text

def analyse_html(html):
    soup = BeautifulSoup(html, "lxml")
    table = soup.find('table', attrs={'id': 'report'})
    trs = table.find("tr").find_next_siblings()
    relist=[]
    for tr in trs:
        tds = tr.find_all("td")
        tdlist=[]
        tdlist.append(tds[0].text.strip())
        tdlist.append(tds[1].text.strip())
        tdlist.append(tds[2].text.strip())
        tdlist.append(tds[3].text.strip())
        tdlist.append(tds[4].text.strip())
        tdlist.append(tds[5].text.strip())
        tdlist.append(tds[6].text.strip())
        tdlist.append(tds[7].text.strip())
        tdlist.append(tds[8].text.strip())
        relist.append(tdlist)
    # print(relist)
    return relist
        # yield [
        #     tds[0].text.strip(),
        #     tds[1].text.strip(),
        #     tds[2].text.strip(),
        #     tds[3].text.strip(),
        #     tds[4].text.strip(),
        #     tds[5].text.strip(),
        #     tds[6].text.strip(),
        #     tds[7].text.strip(),
        #     tds[8].text.strip(),
        # ]



# def write_to_file(content):
#     with codecs.open('fayuaninfo.txt', "a", encoding='utf-8') as p:
#         p.write(json.dumps(content, ensure_ascii=False)+'\n')
def connect():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='courtinfo',
        charset='utf8',
    )
    return conn

def write_to_mysql(content,cur):
    # print(content)
    cur.executemany("insert into court(Court_of_law, court, dtime, case_no, cause_of_action, und_t_dep, persiding_judge, plaintiff, defendant)VALUES(%s, %s, %s,%s,%s,%s,%s,%s,%s)",content)


def months(dt, months):  # 这里的months 参数传入的是正数表示往后 ，负数表示往前
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12+1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    dt = dt.replace(year=year, month=month, day=day)
    return dt


def get_page_nums():
    url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp"
    dateTime = datetime.date.fromtimestamp(time.time())
    # nextdate = months(dateTime, 1)
    data = {
       'ktrqks': dateTime,
       'ktrqjs': dateTime,
    }
    html = get_html(url, data)
    soup = BeautifulSoup(html, "lxml")
    if soup.body.text.strip() == "系统繁忙":
        print("系统繁忙,登录次数过多,IP被禁止")
        time.sleep(ERROR_SLEEP_TIME)
    else:
        pass
    div = soup.find("div", {"class": "meneame"})
    page_nums = div.find('strong').text
    page_nums = int(page_nums)
    if page_nums % 15 == 0:
        page_nums = page_nums // 15
    else:
        page_nums = page_nums // 15 + 1
    print("总页数为: %s" % str(page_nums))
    return page_nums
def main():
    page_nums = get_page_nums()
    base_url = "http://www.hshfy.sh.cn/shfy/gweb/ktgg_search_content.jsp"
    dateTime = datetime.date.fromtimestamp(time.time())
    # nextdate = months(dateTime, 1)
    page_num = 1
    data = {
        'ktrqks': dateTime,
        'ktrqjs': dateTime,
        'pagesnum': page_num,
    }
    conn = connect()
    cur = conn.cursor()
    while page_num <= 10:
        # print(data)
        html = get_html(base_url, data)
            # soup = BeautifulSoup(html, 'lxml')
            # if soup.body.text.strip() == "系统繁忙":
            #     print("系统繁忙，登录太频繁，ip被封锁")
            #     time.sleep(ERROR_SLEEP_TIME)
            #     continue
            # else:
            #     break
        result = analyse_html(html)
        # for res in result:
        # write_to_mysql(res, cur)
        write_to_mysql(result, cur)
        print("写入第 %s 页,共 %s 页" % (page_num, page_nums))
        page_num += 1
        data["pagesnum"] = page_num
        time.sleep(1)
    else:
        cur.close()
        conn.commit()
        conn.close()
        print("爬取完毕")
    print("开始休眠...")
    time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
    print("Done!")
