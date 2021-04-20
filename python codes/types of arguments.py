def add(a,b):
	c=a+b
	print(c)


add(2,5)

def person(name,age):
	print(name)
	print(age)

person(name='Thangamani',age=21)

def person(name,age=18):
	print(name)
	print(age)

person('Thangamani',)

def sum(a, *b):
	c=a
	
	for i in b:
	    c=c+i
	print(c)

sum(4,7,78,89)

