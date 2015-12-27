# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, os

def setDriver():
# Firefox Profile を定義 ############################################################
  # Firefox プロファイルの準備
  profile = webdriver.FirefoxProfile()
  # ダウンロード先の指定 0:デスクトップ、1:>システム既定フォルダ、2:ユーザ定義フォルダ（"browser.download.dir"で定義）
  """
  profile.set_preference('browser.download.folderList', 0)
  """
  # ブラウザのダウンロードディレクトリ(スクリプトが存在するディレクトリ)を指定
  profile.set_preference('browser.download.dir', os.getcwd()+"/malwr")
  
  # ダウンロード時の警告画面を表示させない
  profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
    'text/csv, text/xls, application/pdf, application/zip, application/xml, text/plain, application/vnd.ms-excel, text/comma-separated-values, application/octet-stream'
    )

#profile.set_preference('browser.download.manager.showWhenStarting', False)
# Firefox がブラウザ内で PDF を開こうとするので無効化
  profile.set_preference('pdfjs.disabled', True)
# サードパーティの PDF ソフトが PDF を開こうとするので無効化
  profile.set_preference('plugin.scan.plid.all', False)
  profile.set_preference('plugin.scan.Acrobat', '99.0')
# Firefox Profile を定義 ############################################################
  driver = webdriver.Firefox(profile)
  return driver
