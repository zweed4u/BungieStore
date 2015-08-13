# -*- coding: utf-8 -*-
import mechanize
import urllib
import cookielib
import BeautifulSoup
import html2text
import re
import sys
import StringIO
from urllib2 import HTTPError
import os
import time
import webbrowser

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]
loop = 1

l_tk = 'http://bungiestore.com/cart/2984134788:1'
l_how= 'http://bungiestore.com/cart/1766901060:1'


print '\nWhich?\n1.) Taken King (large)\n2.) House Of Wolves (large)\nPlease enter a number: '
choice = raw_input('')
print '\n'

if choice == "1":
	url = l_tk
elif choice == "2":
	url = l_how
else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()




print "Running..."
print "Target: " + str(url.split('//')[1].split('.com')[0].upper())
print "Using variant: " + str(url[:-2].split("/")[len(url[:-2].split("/"))-1])+ "\n"
while (1==1):
    try:
        br.open(str(url))
        '''
        for f in br.forms():
            print f

        '''
        if str(url) in str(br.geturl()):
            print "Try: " + str(loop) + " - MOST LIKELY OOS =( ..."
            print "--> " + str(br.geturl()) +"\n"
 
        br.select_form(nr=0)
        redirect=str(br.geturl())
        if "stock_problems" in str(br.geturl()):
            print "Try: " + str(loop) + " - ATC NOT LIVE YET..."
            print "--> " + str(br.geturl()) +"\n"
            loop+=1
	    time.sleep(4)
        else:
            print "Try: " + str(loop) + " - Success!!! LEMME GET THAT CART FOR YOU"
            webbrowser.open(str(redirect))
            print "--> " + str(br.geturl()) +"\n"
            #Maybe implement a -4 to variant to atc next size down or up next time
            #redeclare url here.
            time.sleep(10)
            #url = "http://XXXXXXXXXXX.com/cart/VAR-4:1"
            loop+=1
    
    except:
        if str(url) in str(br.geturl()):
            print "Try: " + str(loop) + " - MOST LIKELY OOS =( ..."
            print "--> " + str(br.geturl()) +"\n"
        else:
            print "Try: " + str(loop) + " - IDK BRUH"
            print "--> " + str(br.geturl())+"\n"
        #time.sleep(1)
        loop+=1
        continue
    
#os.system("pause")



