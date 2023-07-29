from Store import store

BASE_URL = r'/Shop.store'


@store.route(BASE_URL + '/test')
def test():
    return 'Hello world!'