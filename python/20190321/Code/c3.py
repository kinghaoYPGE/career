import asyncio
import threading

@asyncio.coroutine
def hello():
  print('hello asyncio! (%s)' % threading.currentThread())
  r = yield from asyncio.sleep(5)
  print('back again!(%s)' % threading.currentThread())

async def hello2():
  print('hello2 asyncio!!!!! (%s)' % threading.currentThread())
  r = await asyncio.sleep(1)
  print('back2 again!!!!!(%s)' % threading.currentThread())

@asyncio.coroutine
def hello3():
  print('hello3 asyncio!!!!! (%s)' % threading.currentThread())
  print('back3 again!!!!!(%s)' % threading.currentThread())

# 得到消息循环对象
loop = asyncio.get_event_loop()
tasks = [hello(), hello2(), hello3()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()