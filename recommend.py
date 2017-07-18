import pymysql
from random import choice

def recommend(user):
    DB = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='recommend', charset='utf8');
    c = DB.cursor()
    # sql语句
    sql = "select anime_id  from user_anime where user_id=%s" % user
    c.execute(sql)
    # 得到结果集
    results = c.fetchall()
    print(results)
    #得到用户喜爱的番剧编号，编号是系统自动存储的，根据该信息进行推荐
    love = []
    for line in results:
        love.append(line[0])
    print(love)

    #从用户喜爱的番剧中找出所有的style依次计数，找出最多出现的三个style
    sql = '''select style_id,count(*) as style_count from anime_style
    where anime_id in (select anime_id  from user_anime where user_id=%s) group by style_id order by style_count desc limit 3''' % user
    c.execute(sql)
    results = c.fetchall()
    print(results)
    style = []
    for line in results:
        style.append(line[0])
    print(style)

    #分别找出同时含有style[0],style[1],style[2]的番剧集合

    sql = '''select anime_id from
            ((select distinct anime_id from anime_style where style_id = {}) as a
            natural join (select distinct anime_id from anime_style where style_id = {}) as b
            natural join (select distinct anime_id from anime_style where style_id = {}) as c
            )
            where anime_id not in (select anime_id  from user_anime where user_id=1);
    '''.format(style[0],style[1],style[2],user)
    c.execute(sql)
    results = c.fetchall()
    print(results)
    recommend_anime = []
    for line in results:
        recommend_anime.append(line[0])
    dic={}
    if(len(recommend_anime)==0):
        dic['name']=dic['brief']='empty'
    else:
        result_anime_id = choice(recommend_anime)
        sql = 'select name,brief from anime where id = {}'.format(result_anime_id)
        c.execute(sql)
        results = c.fetchall()
        print(results)
        dic={}
        dic['name'] = results[0][0]
        dic['brief'] = results[0][1]
        print(dic)
    DB.close()
    return dic

if __name__=='__main__':
    recommend(1)
# 连接数据库
#db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='recommand', charset='utf8')

#cursor = db.cursor()
#sql = ""

#cursor.execute(sql)

#db.close()