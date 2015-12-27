# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
import time, os, os.path

# import my script
import displayMod
import browserMod
import malwrLogin as Login
import malwrGet

def dirCheck():
  if os.path.isdir("./malwr"):
    pass
  else:
    os.makedirs("./malwr")
  return
  
def pyEnd(driver, display):
  print "Script End."
  # quit driver
  if driver is not None:
    driver.close()
    driver.quit()
  # stop virtual display
  if display is not None:
    display.stop()
  return

def main():
  try:
    print "Set Virtual Display",
    display = displayMod.setDisplay()
    print "-> success"
    print "Set Browser Profile",
    driver = browserMod.setDriver()
    print "-> success"
    driver = Login.login(driver)
    driver,urls = malwrGet.getDlUrls(driver)
    #print urls
    driver = malwrGet.getMalware(driver, urls)
    driver = Login.logout(driver)

    pyEnd(driver, display)

  except:
    print "-----!!!Error occured!!!-----"
    Login.logout(driver)
    pyEnd(driver, display)
    pass
  return

if __name__ == '__main__':
  dirCheck()
  main()
