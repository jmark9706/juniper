#!/usr/bin/python
import cgi
from datetime import datetime
import cgitb
import time
import os
import sys
import  string
from cgi import escape
 
cgitb.enable()
# get q parm
form = cgi.FieldStorage()
# check for no query parm
try:
    src= form['s'].value
except:
    src="0"

image = open('1px.png', 'rb') #open binary file in read mode
img = image.read() 

image.close()
slen=len(img)
ls = "Content-Length: "+str(slen)+"\r\n"

sys.stdout.write( "Content-Type: image/jpeg\r\n")
sys.stdout.write(ls)
sys.stdout.write("Connection: close"+"\r\n")
sys.stdout.write("\r\n")

sys.stdout.write(img)
ua=os.getenv('HTTP_USER_AGENT')

host=os.getenv('HTTP_HOST')

logprefix='/var/www/log/'
# entire transaction
fs = open('/var/www/log/mlogger','a')
fs.write("***** client="+src+ " : "+host)
fs.write(' : ')
fs.write(ua)
fs.write(' : ')
st = str(datetime.now())
fs.write(st)
fs.write("\r\n")
fs.write("image=binary"+ " Len="+str(slen))
fs.write('\n\r\n')
fs.close()
#  get the time we are logging
#xsecs=time.time()


#sys.stdout.write("\r\n")



