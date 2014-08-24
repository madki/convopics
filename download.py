import urllib

f = open('links.txt', 'r')
links = f.readlines()
f.close()
g = open('links.csv', 'w')
i = 0
for link in links:
	arr = link.split('  ')
	if (len(arr)==2):
		i += 1
		print "downloading " + str(i) + ".jpg"
		piclink = arr[1].replace('\n', '')
		resource = urllib.urlopen(piclink)
		output = open("images/"+str(i)+".jpg","wb")
		output.write(resource.read())
		output.close()
		g.write(str(i)+','+piclink)
g.close()