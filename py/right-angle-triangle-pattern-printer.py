def myfunc(ch,n):
	for i in range(0, n):
		for j in range(0, i+1):
			print("%s " % ch,end="")
		print("\r")

ch = input('Enter the pattern character:') or '*'
n = int(input('Enter the pattern size:'))
myfunc(ch,n)
