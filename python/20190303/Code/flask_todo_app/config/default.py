class Config(object):
  BEBUG = False
  
  SECRET_KEY = 'default'
  
  MONGODB_SETTINGS = {
  'db': 'todo_db',
  'host': '127.0.0.1',
  'port': 27017
  }
  
  SITE_DOMAIN = 'http://172.0.0.1:8089'
