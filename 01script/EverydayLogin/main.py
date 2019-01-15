import os
import sys
import linecache
import configparser
from time import sleep
import pyautodroid as pad


#print("初期設定")
imgfile = "C:/Users/jesc1/Nox_share/ImageShare/img/login/"
device = '127.0.0.1:62001'

os.system("nox_adb -s "+device+" shell am start -n jp.co.mixi.monsterstrike/.MonsterStrike")

os.system("nox_adb shell wm density 120")
