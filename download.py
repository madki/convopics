import urllib

f = open('links.txt', 'r')
links = f.readlines()
f.close()
g = open('links.csv', 'a')
i = 0
n = 4401
for link in links:
	arr = link.split('  ')
	if (len(arr)==2) & (i<n):
		print "skipped " + str(i)
		i += 1
	if (len(arr)==2) & (i==n):
		print "downloading " + str(i) + ".jpg "
		piclink = arr[1].replace('\n', '')
		print piclink
		resource = urllib.urlopen(piclink)
		output = open("images/"+str(i)+".jpg","wb")
		output.write(resource.read())
		output.close()
		g.write(str(i)+','+piclink)
		i += 1
	if (len(arr)==2) & (i>n):
		i += 1
		print "downloading " + str(i) + ".jpg "
		piclink = arr[1].replace('\n', '')
		print piclink
		resource = urllib.urlopen(piclink)
		output = open("images/"+str(i)+".jpg","wb")
		output.write(resource.read())
		output.close()
		g.write(str(i)+','+piclink)
g.close()