#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kazuhiro
#
# Created:     14/07/2013
# Copyright:   (c) Kazuhiro 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def bubble_sort(src):
    length = len(src)
    for i in range(length):
        x = 0
        while x < length - 1:
            if src[x] > src[x + 1]:
                tmp = src[x]
                src[x] = src[x + 1]
                src[x + 1] = tmp
            x += 1


def main():
    pass

if __name__ == '__main__':
    main()
    array = [10,8,3,6,7,11,19,15,21,9,3,4,1]
    bubble_sort(array)
    for i  in range(len(array)):
        print(array[i])