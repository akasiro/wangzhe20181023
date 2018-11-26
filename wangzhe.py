# -*- coding: utf-8 -*-
import os
from time import sleep
from PIL import Image
import cv2#opencv


def tap_screen(x,y):
    os.system('adb -s 53faa9d3 shell input tap {} {}'.format(x,y))




if __name__ =='__main__':
    for i in range(60):
        if i>0:
            tap_screen(2489,1307) #再次挑战
            sleep(5)
        tap_screen(1465,913)#闯关
        sleep(10)
        tap_screen(1795,40)#自动
        sleep(27)
        tap_screen(1795, 40)#点击跳过
        sleep(2)
        tap_screen(1795, 40)  # 点击跳过
        sleep(5)
        tap_screen(500, 500)  # 点击继续
        sleep(5)
        tap_screen(1588,975) #再次挑战
        sleep(1)

