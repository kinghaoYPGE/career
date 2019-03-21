def consumer():
  r = ''
  while True:
    n = yield r
    if not n:
      return
    print('[consumer]: %s' % n)
    r = '200 OK'

def produce(c):
  c.send(None)
  n = 0
  while n < 5:
    n += 1
    print('[product]: %s' % n)
    r = c.send(n)
    print('[product]: %r' % r)
  c.close()

c = consumer()
produce(c)
