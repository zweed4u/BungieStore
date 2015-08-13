import urllib, json, sys
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

response = urllib.urlopen(jsonurl)
data = json.loads(response.read())
#print data


#enumerate how many colors
numcolorways=len(data.values()[0].values()[14])

for i in range(numcolorways):
	cwinfo=(data.values()[0].values()[14][i]) 
	print str(cwinfo[u'title']).rjust(6)+" :: Inventory - " +str(cwinfo[u'inventory_quantity'])+ " :: Checkout link - http://bungiestore.com/cart/"+str(cwinfo[u'id'])+':1'

print '\n'


