# -*- coding: utf-8 -*-
import os
from time import sleep
from PIL import Image
#import cv2#opencv
import random

def tap_screen(x,y):
    os.system('adb -s 53faa9d3 shell input tap {} {}'.format(x,y))



if __name__ =='__main__':
    total = input('刷本次数： ')
    print('开始刷本')
    for i in range(int(total)):
        if i>0:
            tap_screen(2489,1307) #再次挑战
            sleep(random.randint(4,6))
        tap_screen(1465, 913)  # 闯关
        sleep(15)
        # if i == 0:
        #     tap_screen(1795, 40)  # 自动

        sleep(random.randint(55,60))
        tap_screen(730,450) #点击任意位置继续
        if random.randint(0,100)%2 == 1:
            tap_screen(720,440)
            tap_screen(725,400)
        sleep(5)
        tap_screen(1588, 975)  # 再次挑战
        sleep(1)
        if i%60 ==0 & i!=0:
            sleep(60)
        print('di {} '.format(i))
    print('complete')
    
