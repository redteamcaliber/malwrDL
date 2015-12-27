# coding: utf-8
import hashlib

def getSha1Hash( malware):
  h = hashlib.sha1()
  while True:
    d = f.read(64*1024) # 64KB
    if ( d ):
      h.update(d)
    else:
      break
  return h.hexdigest()

def saveMalware():
  for 
  f = open( "./malware/" + malware, "rb")
  f.close()
  
