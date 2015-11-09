from aiohttp import web
from main import db

class Handler:

    def __init__(self):
        pass

    def handle_intro(self, request):
        return web.Response(body=b"Hello, world")

    async def do_insert(self, value):
        document = {'key': value}
        result = await db.test_collection.insert(document)
        return result

    async def handle_greeting(self, request):
        name = request.match_info.get('name', "Anonymous")
        result = await self.do_insert(name)
        txt = "Hello, {}".format(name)
        return web.Response(text=txt)

handler = Handler()
