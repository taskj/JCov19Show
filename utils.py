import time
import pymysql

def get_time():
    time_str = time.strftime("%Y {} %m {} %d {} %X")
    return time_str.format("年","月","日")

def get_conn():
    #创建连接
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="",
        db="jcov19show",
        charset="utf8"
    )

    #创建游标
    cursor = conn.cursor()
    return conn,cursor

def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    '''
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果
    '''
    conn,cursor = get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

def get_c1_data():
    sql = "select sum(confirm),sum(heal),sum(dead) from details where update_time=(select update_time from details order by update_time desc limit 1)"
    res = query(sql)
    return res[0]

def get_c2_data():
    sql="select province,sum(confirm) from details where update_time=(select update_time from details order by update_time desc limit 1) group by province"
    res = query(sql)
    return res

def get_l1_data():
    sql = "select sum(confirm),update_time from details "\
          "group by update_time "\
          "order by update_time desc limit 5"
    res = query(sql)
    return res

def get_l2_data():
    sql = "select sum(heal),sum(dead),update_time from details "\
          "group by update_time "\
          "order by update_time desc limit 5"
    res = query(sql)
    return res

def get_r1_data():
    '''
    联合查询数据库中最新一天数据的top5
    :return:
    '''
    sql="SELECT city,confirm FROM "\
        "(select city,confirm from details "\
        "where update_time=(select update_time from details order by update_time limit 1) "\
        "and province not in('北京','重庆','天津','上海') "\
        "union all "\
        "select province as city,sum(confirm) as confirm from details " \
        "where update_time=(select update_time from details order by update_time limit 1) "\
        "and province in('北京','重庆','天津','上海') group by province) as a "\
        "order by confirm DESC limit 5"
    res = query(sql)
    return res

def get_r2_data():
    sql = "select content from hotsearch order by id desc limit 20"
    res = query(sql)
    return res

if __name__ == '__main__':
    get_l2_data()