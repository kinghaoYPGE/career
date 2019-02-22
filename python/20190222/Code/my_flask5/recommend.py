import MySQLdb
from functools import reduce

def recommend(user):
  # 连接数据库
  db = MySQLdb.connect('localhost', 'root', '', 'recommend')
  cur = db.cursor()
  # 1. 查询当前user喜欢的电影(user, user_movie)
  favorite = set()
  sql = 'select movie_id from user_movie where user_id = %s' % user
  cur.execute(sql)
  # 结果集
  results = cur.fetchall()
  for r in results:
    favorite.add(r[0])
  print(favorite)
  if len(favorite) == 0:
    return None
  # 2. 查询上面电影的类别,统计排序,取前三个类别 (movie_style)
  sql = '(select style_id,movie_id from movie_style where movie_id in(%s)' \
          % ','.join([str(i) for i in favorite])+')'
  sql = 'select style_id from '+ sql +' temp group by temp.style_id order by count(*) desc limit 3'
  cur.execute(sql)
  results = cur.fetchall()

  # 3. 找到同时具备这三个类别的电影推送给用户(用户喜欢的电影排除在外)
  movies = set()
  movie_set_list = []

  for r in results:
    sql = 'select movie_id from movie_style where movie_id not in(%s) and style_id = %s' % (','.join([str(i) for i in favorite]), r[0])
    cur.execute(sql)
    results = cur.fetchall()
    movie_set = set()
    for r in results:
      movie_set.add(r[0])
    movie_set_list.append(movie_set)  # [{123, 111, 124}, {123, 119, 128}, {123, 112, 124}]
  # 取set的交集(同时具备<=3个类别的电影)
  s = set(reduce(lambda s1, s2: s1 & s2, movie_set_list))
  if len(s) == 0:
    s = set(movie_set_list[0])
  print(s)
  
  sql = 'select name, brief from movie where id in(%s)' % ','.join([str(i) for i in s])
  cur.execute(sql)
  results = cur.fetchall()
  print(results)
  movie_dict_list = []
  for i, j in results:
    movie_dict = {}
    movie_dict['name'] = i
    movie_dict['brief'] = j
    movie_dict_list.append(movie_dict)
  db.close()
  return movie_dict_list

if __name__ == '__main__':
  recommend(1)
