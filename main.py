# Copyright 2015 VapeShop Engine, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
from aiohttp import web
from grab_routes import routerutil
from db_engine import db
from settings import *
from apps.account import routes
from apps.blog import *
from apps.contacts import *
from apps.eliquidsconstuctor import *
from apps.faq import *
from apps.shop import routes

# TODO Refactoring for DEBUG MODE

if DEBUG_MODE:
    import aiohttp_debugtoolbar
    from aiohttp_debugtoolbar import toolbar_middleware_factory

def create_middlewares_list():
    if DEBUG_MODE:
        debug_middle = [toolbar_middleware_factory, ]
    prod_middle = []
    p = prod_middle + debug_middle
    return p

async def init(loop):
    app = web.Application(loop=loop,
                          middlewares=create_middlewares_list())
    if DEBUG_MODE:
        aiohttp_debugtoolbar.setup(app)
    for i in routerutil.routes_list:
        app.router.add_route(*i)

    srv = await loop.create_server(app.make_handler(), HOST_ADDR, HOST_PORT)
    print("Server started at http://{0}:{1}".format(HOST_ADDR, HOST_PORT))
    return srv

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
