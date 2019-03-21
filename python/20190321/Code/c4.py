from aiohttp import web
import asyncio

async def index(reuqest):
  print('index...')
  await asyncio.sleep(5)
  return web.Response(body='<h1>Index</h1>')

async def hello(request):
  print('hello...')
  await asyncio.sleep(5)
  return web.Response(body='<h1>Hello %s </h1>' % request.match_info['name'])

async def init(loop):
  app = web.Application(loop=loop)
  app.router.add_route('GET', '/', index)
  app.router.add_route('GET', '/hello/{name}', hello)
  server = await loop.create_server(app.make_handler(), '127.0.0.1', 5000)
  print('Server started at 127.0.0.1:8000...')
  return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()