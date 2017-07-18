import pymysql

# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='recommand', charset='utf8')

cursor = db.cursor()
sql = "create table user_anime(user int,anime int)"
cursor.execute(sql)
db.close()