

a=10

def something():
    a=15

    print("inside function" ,a)


something()

print("outside function",a)




a=10

print(id(a))

def something():
	a=9

	x=globals()['a']
	print(id(x))
	print("inside function",a)


something()
print("outside function",a)

a=10

print(id(a))

def something():
	a=9

	x=globals()['a']
	print(id(x))
	print("inside function",a)

globals()['a']= 15

something()
print("outside function",a)