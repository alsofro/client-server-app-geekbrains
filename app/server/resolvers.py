from functools import reduce
from settings import INSTALLED_MODULES

def get_server_actions():
    modules = reduce(
        lambda value, item: value + [__import__('{}.actions'.format(item))],
        INSTALLED_MODULES, []
    )

    # print(modules)

    submodules = reduce(
        lambda value, item: value + [getattr(item, 'actions', [])],
        modules, []
    )

    # print(submodules)

    actionnames =  reduce(
        lambda value, item: value + getattr(item, 'actionnames', []),
        submodules, []
    )

    # print(actionnames)


    return {itm.get('action'): itm.get('controller') for itm in actionnames}

def resolve(action_name, actions=None):
    actionnames = actions or get_server_actions()
    return actionnames.get(action_name)




if __name__ == '__main__':
    print(get_server_actions())
    print(resolve('echo'))