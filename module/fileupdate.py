import os
import urllib.request
url = ("https://raw.githubusercontent.com/ryuryu13y/selenium/master/main.py")

save_name = ("main.py")

# ダウンロードする
mem = urllib.request.urlopen(url).read()

# ファイルへの保存
with open(save_name, mode="wb") as f:
    f.write(mem)
