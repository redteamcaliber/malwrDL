# coding: utf-8
import lxml.html
from lxml import etree

def sha1txt( dom):
  sha_dom = dom.get_element_by_id('file').xpath(u".//*[contains(text(), 'SHA1')]")
  return sha_dom[0].getparent().xpath(u"./td")[0].text
