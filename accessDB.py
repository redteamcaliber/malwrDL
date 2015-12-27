# coding: utf-8

import MySQLdb

db = "malwaredb"

def loginDB():
  ### DB へログイン
  con = MySQLdb.connect(db = db)
  return con, con.cursor()

def searchDB( sha1):
  con, cursor = loginDB()
  # search query
  cursor.execute("select sha1 from malware_data where sha1 = " + sha1)
  result = cursor.fetchall()

  for row in result:
    print row

  """
  if :
    return True
  return False
  """
  con.close()
  return

def insertDB( sha1, maltype):
  con, cursor = loginDB()

  # insert query
  try:
    cursor.execute("insert to malware_data( sha1, type) values(" +  sha1 + "," + maltype + ")")
    con.commit()
  except:
    con.rollback()

  con.close()
  return
