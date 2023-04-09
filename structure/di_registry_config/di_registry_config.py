"""
https://seddonym.me/2019/08/03/ioc-techniques/
"""

from structure.di_registry_config import hello_world

hello_world.config['OUTPUT_FUNCTION'] = print

if __name__ == '__main__':
    hello_world.hello_world()
