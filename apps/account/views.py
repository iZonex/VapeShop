from aiohttp import web


class MemberView:

    async def profile(self, request):
        return web.Response(text='profile')

    async def login(self, request):
        return web.Response(text='login')

    async def logout(self, request):
        return web.Response(text='logout')

    async def register(self, request):
        return web.Response(text='register')

    async def reg_confirm(self, request):
        return web.Response(text='reg confirm')

memberview = MemberView()


class MemberAdminView:

    async def create(self, request):
        return web.Response(text='create')

    async def get_member(self, request):
        return web.Response(text='member')

    async def get_members(self, request):
        return web.Response(text='members')

    async def remove(self, request):
        return web.Response(text='remove')

memberadmin = MemberAdminView()
