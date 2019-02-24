需求: ‘猜你喜欢’推荐系统
需求分析: 
  1. 查询当前user喜欢的电影(user, user_movie)
  2. 查询上面电影的类别,统计排序,取前三个类别 (movie_style)
  3. 找到同时具备这三个类别的电影推送给用户(用户喜欢的电影排除在外)(movie_style,user_movie)
  4. 展示给用户(movie)
技术选型: 技术栈: Flask, Mysql
模型设计: user, movie, user_movie, movie_style)
项目结构: tree
业务逻辑: 开发过程, 本地测试
测试
部署