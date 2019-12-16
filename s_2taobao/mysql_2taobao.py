import pymysql


class ConnMysql(object):
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host='localhost',
                                  port=3306,
                                  database='xianyu',
                                  user='root',
                                  password='',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def insert(self, dict1):
        # 将数据添加到数据库中的movie表中
        sql = "insert into product(category, time, title, price, quality, address, img_list, introduction) " \
              "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        data = [dict1['category'], dict1['time'], dict1['title'], dict1['price'], dict1['quality'], dict1['address'],
                dict1['img_list'], dict1['introduction']]
        self.cursor.execute(sql, data)
        self.db.commit()