__author__ = 'lijiayan'

from func.func1 import add as add_import, move as mv_import

# 导入所有函数
from func.func1 import *

if __name__ == '__main__':
    add_import(1, 2, 3, 4, 5, 6)
    print(mv_import(1, 2, 5, 50))
