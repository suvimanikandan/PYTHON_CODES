

def person(name,**data):


    print(name)
   
    for i,j in data.items():
   	   print(i,j)


person('swetha',age=24,city='Chidambaram',mob=8903098719)