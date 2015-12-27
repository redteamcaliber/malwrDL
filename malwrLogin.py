# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass

 # ログイン
def login(driver):
  driver.get("https://malwr.com/account/login/")
  print "==========================="
  print "|  access to Login page.  |"
  print "==========================="
  element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "id_username")))
  print("access success.")

  ##### Login to malwr.com ###
  ## input username
  driver.find_element_by_id("id_username").clear()
  driver.find_element_by_id("id_username").send_keys(raw_input('your username: '))
  ## input password
  driver.find_element_by_id("id_password").clear()
  driver.find_element_by_id("id_password").send_keys(getpass('your password: '))
  ## click "Login" button
  driver.find_element_by_css_selector('body > div.container-fluid > form > div:nth-child(5) > div > button').click()

  ## wait for locating topmenu
  element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "wordcloud")))

  print("Login success.")
  return driver

def logout(driver):
  print "==========================="
  print "|       Try Logout.       |"
  print "==========================="
  
  # logout
  driver.get("https://malwr.com/account/logout/")
  ## wait for locating topmenu
  element = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "wordcloud")))

  print("Logout success.")
