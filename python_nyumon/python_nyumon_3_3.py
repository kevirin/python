#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kazuhiro
#
# Created:     15/07/2013
# Copyright:   (c) Kazuhiro 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

    a = 10
    b = a       # ここまでaとbは同じオブジェクト
    a = 20      # 値の代入でaは別オブジェクト
    print(a)
    print(b)
    # aと20は同じオブジェクト
    print('a id is', id(a))
    print('20 id is', id(20))
    c = []
    d = []
    print(id(c))
    print(id(d))