import datetime

# f = open('date.txt','w')

def date1():
	y = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	print(y)
	f = open('date.txt','a')
	print (type(y))
	# print (l)
	f.write(y + '\n')
	f.close()
	return y




date1()