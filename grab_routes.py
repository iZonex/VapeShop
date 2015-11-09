
class RouterUtil:

    routes_list = []

    __instance = None

    def __new__(cls):
        if RouterUtil.__instance is None:
            RouterUtil.__instance = object.__new__(cls)
        return RouterUtil.__instance

routerutil = RouterUtil()
