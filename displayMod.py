# coding: utf-8
from pyvirtualdisplay import Display

# Browser に Firefox を使用する際の設定
# Python の仮想ディスプレイモジュールを用意し、起動
# ここに Firefox を表示させる
def setDisplay():
  display = Display(visible=0, size=(1920, 1080))
  display.start()
  return display
