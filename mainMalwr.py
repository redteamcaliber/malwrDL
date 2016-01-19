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
  
def pyEnd(myDriver, display):
  print "Script End."
  # quit myDriver
  if myDriver is not None:
    myDriver.close()
    myDriver.quit()
  # stop virtual display
  if display is not None:
    display.stop()
  return

def main():
  print "Set Virtual Display",
  display = displayMod.setDisplay()
  print "-> success"
  print "Set Browser Profile",
  myDriver = browserMod.setDriver()
  print "-> success"
  try:
    myDriver = Login.login(myDriver)
    myDriver,urls = malwrGet.getDlUrls(myDriver)
    #print urls
    myDriver = malwrGet.getMalware(myDriver, urls)
    myDriver = Login.logout(myDriver)

    pyEnd(myDriver, display)

  except:
    print "\n-----!!!Error occured!!!-----"
    Login.logout(myDriver)
    pyEnd(myDriver, display)
    pass
  return

if __name__ == '__main__':
  dirCheck()
  main()
