import urllib, json, sys, time, datetime

tk='http://bungiestore.com/collections/e3-2015-collection/products/the-taken-king-t-shirt-men'
how='http://bungiestore.com/collections/featured-house-of-wolves-collection/products/house-of-judgement-t-shirt-men'

print '\nWhich?\n1.) TakenKing\n2.) HouseOfWolves \nPlease enter a number: '
choice = raw_input('')
print '\n'

if choice == "1":
	jsonurl = tk+".json"
elif choice == "2":
	jsonurl = how+".json"
else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()

print 'Size?\n1.) XS\n2.) Small\n3.) Medium\n4.) Large\n5.) XL\n6.) 2XL\n7.) 3XL\n8.) 4XL \nPlease enter a number: '
sizeNum = raw_input('')

if sizeNum == "1":
	size = 'xs'
elif sizeNum == "2":
	size = 'small'
elif sizeNum == "3":
	size = 'medium'
elif sizeNum == "4":
	size = 'large'
elif sizeNum == "5":
	size = 'xl'
elif sizeNum == "6":
	size = '2xl'
elif sizeNum == "7":
	size = '3xl'
elif sizeNum == "8":
	size = '4xl'
else:
	print "Rerun and enter one of the listed numbers above..."
	sys.exit()

response = urllib.urlopen(jsonurl)
data = json.loads(response.read())

#enumerate how many colors
numcolorways=len(data.values()[0].values()[14])

for i in range(numcolorways):
	cwinfo=(data.values()[0].values()[14][i]) 
	#print str(cwinfo[u'title']).rjust(6)+" :: Inventory - " +str(cwinfo[u'inventory_quantity'])+ " :: Checkout link - http://bungiestore.com/cart/"+str(cwinfo[u'id'])+':1'
	###ADDED###
	if str(cwinfo[u'title']).lower()==str(size):
		while cwinfo[u'inventory_quantity']==0:	
			#while - maybe function
			#None in stock - prompt & recheck/loop
			print datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%Y %H:%M:%S') + " :: No " + str(size).upper()+"s in stock - rechecking in 5 seconds"
			time.sleep(5)
			#loop and recheck
		if cwinfo[u'inventory_quantity']!=0:
			#inventory exists! open in webbrowser
			print str(cwinfo[u'inventory_quantity']) + ' ' + str(size) + ' are available! - http://bungiestore.com/cart/'+str(cwinfo[u'id'])+':1'
		else:
			#jump to while
			pass
	else:
		pass
	###########
print '\n'
