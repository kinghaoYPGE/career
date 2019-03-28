from sanic import Sanic
from sanic.response import json
import asyncio
import time

app = Sanic()


@app.route('/')
async def test(request):
    # print(dir(request))
    print(time.time())
    await asyncio.sleep(3)
    print(time.time())
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
