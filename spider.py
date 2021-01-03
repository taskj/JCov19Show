from selenium.webdriver import Firefox,FirefoxOptions
import requests
import json
import utils
import time
import traceback
import sys

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


#获取腾讯疫情数据方法
def tencent_get_details():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    res = requests.get(url, headers)
    d = json.loads(res.text)
    data_all = json.loads(d["data"])
    '''
    字典数据中的的key
    print(data_all.keys())
    dict_keys(['lastUpdateTime', 'chinaTotal', 'chinaAdd', 'isShowAdd', 'showAddSwitch', 'areaTree'])
    '''
    details = []
    update_time = data_all['lastUpdateTime']
    data_country = data_all['areaTree']
    data_province = data_country[0]['children']
    for pro_infos in data_province:
        province = pro_infos['name'] #省名
        for city_infos in pro_infos['children']:
            city = city_infos['name'] #城市名
            confirm = city_infos['total']['confirm'] #确诊人数
            confirm_add = city_infos['today']['confirm'] #当日新增确诊人数
            heal = city_infos['total']['heal'] #治愈人数
            dead = city_infos['total']['dead'] #死亡人数
            details.append([update_time,province,city,confirm,confirm_add,heal,dead])
    update_details(details)

def update_details(details):
    try:
        conn, cursor = utils.get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,heal,dead) values (%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s=(select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query,details[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新数据")
            for item in details:
                cursor.execute(sql,item)
            conn.commit()
            print(f"{time.asctime()}数据更新完毕")
        else:
            print(f"{time.asctime()}当前已经是最新数据")
    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)


#获取新浪热搜方法
def get_sina_hot():
    option = FirefoxOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    broswer = Firefox(options=option,executable_path="C:\Program Files\Mozilla Firefox\geckodriver.exe")
    url = "https://s.weibo.com/top/summary"
    broswer.get(url)
    res = broswer.find_elements_by_xpath("//*[@id='pl_top_realtimehot']/table/tbody/tr")
    context = []
    for i in res:
        data = i.find_element_by_class_name("td-02").text
        context.append(data)
    update_hotsearch(context,broswer)

def update_hotsearch(context,broswer):
    cursor = None
    conn = None
    try:
        print(f"{time.asctime()}数据更新完毕")
        conn,cursor = utils.get_conn()
        sql = "insert into hotsearch(dt,content) values(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql,(ts,i))
        conn.commit()
        print(f"{time.asctime()}数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)
        broswer.quit()




if __name__ == '__main__':
    l = len(sys.argv)
    if l == 1:
        s = """
        请输入参数
        up_cov 更新最新疫情数据
        up_hot 更新最新热搜
        """
        print(s)
    else:
        order = sys.argv[1]
        if order == "up_cov":
            tencent_get_details()
        else:
            get_sina_hot()

