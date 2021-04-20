from numpy import *
 
arr1=array([2,4,5,6,7,9])

arr2=arr1.copy()

arr1[1]  =5

print(arr1)

print(arr2)

print(id(arr1))

print(id(arr2))