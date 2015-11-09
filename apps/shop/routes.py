from .view import handler
from grab_routes import routerutil


routerutil.routes_list.append(('GET', '/test/{name}', handler.handle_greeting))
