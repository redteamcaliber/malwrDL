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
import lxml.html
from lxml import etree
import time
import mysql
import getSha1

def getDlUrls(driver):
  malUrlList = []

  driver.get("https://malwr.com/analysis/")
  print "=================================="
  print "|  access to Malware List page.  |" 
  print "=================================="
  element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "footer-extra")))
  print("[access] success.")

  ### get Html source
  #print driver.page_source
  #print "make dom data", 
  dom = lxml.html.fromstring(driver.page_source)
  #print "-> success."
  #print "Get 'a' elements",
  tbody = dom.xpath('//a')
  #print "-> success."
  #print "------------------------------------------"
  for anchor in tbody:
    if anchor.text is None and anchor.attrib.has_key('href'):
      # links returns belows
      # /analysis/Mjc5ZTdlMmRmYTZiNGIyNGI3NzcwZjg5MWIzMmQ5ZDM/
      #print type(anchor.attrib['href'])
      if "analysis" in anchor.attrib['href']:
        malUrlList.append("https://malwr.com" + anchor.attrib['href'])

  print "[Get URL List] success."
  return driver, malUrlList

def dlTest( driver, urls):
  print "----------------------------"
  print "|  This is download test.  |"
  print "----------------------------"

  cnt = 5
  db = mysql.mysql()
  for url in urls:
    driver.get(url)
    print "  access to", url,
    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "file")))
    print "-> suceess."

    ### Error Text check###
    if '<li class="text-error">' in driver.page_source:
      print "  This malware has error text."
      errorText = driver.find_element_by_class_name('text-error')
      print errorText.text
    
    ### make dom data ###
    print "    Get dom",
    dom1 = lxml.html.fromstring(driver.page_source)
    print "-> executed."

    ### make dom data ###
    print "    Get SHA-1",
    sha1 = getSha1.sha1txt( dom1)
    if not db.mysql_insert(sha1):
      time.sleep(20)
      if not virustotal_search.virustotal_api( db, sha1):
        pass
    #print "-> executed. :", sha1
      else:
        downloadClick( driver, dom1)

    ### Get anchors to Donwload Bottun
    downloadClick( driver, dom1)
    cnt -= 1
    if cnt == 0:
      break

def downloadClick( driver, dom):
  ### Get anchors to Donwload Bottun
  dlButton = dom.xpath(u"//a[contains(text(), 'Download')]")
  for anchor in dlButton:
    #-----#
    if anchor.attrib.has_key('disabled'):
      print "  This file is not shared :-<"
    else:
      #-----#
      if "/analysis/file" in anchor.attrib['href']:
        print "    Download url -> ", anchor.attrib['href']
        driver.execute_script('window.scrollTo(0, 300)')
        driver.find_element_by_xpath(u"//a[contains(text(), 'Download')]").click()
        time.sleep(1)
      #-----#
    #-----#
  time.sleep(1)

def getMalware(driver, urls):

  print "=================================="
  print "|   access to Malware DL page.   |" 
  print "=================================="
  
  # This function is download test for debug
  dlTest( driver, urls)

  """

  # connect to malware database
  db = mysql.mysql()

  for url in urls:
    driver.get(url)
    print "  access to", url,
    element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "file")))
    print "-> suceess."

    ### Error Text check###
    if '<li class="text-error">' in driver.page_source:
      print "  This malware has error text."
      errorText = driver.find_element_by_class_name('text-error')
      print errorText.text
    
    ### make dom data ###
    print "    Get dom",
    dom1 = lxml.html.fromstring(driver.page_source)
    print "-> suceess."

    ### make dom data ###
    print "    Get SHA-1",
    sha1 = getSha1.sha1txt( dom1)
    if not db.mysql_insert(sha1):
      time.sleep(20)
      if not virustotal_search.virustotal_api( db, sha1):
        pass
    #print "-> executed. :", sha1
      else:
        downloadClick( driver, dom1)
  """
  return driver
