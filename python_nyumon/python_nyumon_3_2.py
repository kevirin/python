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

# 関数定義
def main():
    pass

def myPrint(x):
    print("argment Value is ", x)


# クラス
class MyClass(object):
    _x = object

    def get():
        return _x
    def set(x):
        _x = x


if __name__ == '__main__':
    main()

    nest = 0
    if nest == 0:
        print('nest')
        nest+=1
        if nest == 1:
            print('____nest')
            nest += 1
        else:
        #必ず１行以上処理をしなければいけない
            pass
    else: pass
    print('out')

    for i in range(3):
        print(i)






