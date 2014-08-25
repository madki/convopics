f = open('links.csv')
lines = f.readlines()
f.close()
g = open('correctedlinks.csv', 'w')

temp = 0
for line in lines:
	arr = line.split(',')
	if (int(arr[0]) - temp) > 1:
		newnum = temp + 1;
		temp = newnum
		g.write(str(newnum)+','+arr[1])
	else:
		temp = int(arr[0])
		g.write(line)