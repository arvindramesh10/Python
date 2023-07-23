
print("TASK 1")
x = [1,2,3]
x.reverse()
print(x) 


print("TASK 2")
x = [1,2,3,4,5]
print("BEFORE")
print(x)
x.pop(0)
x.pop(3)
x.append(1)
x.insert(0,5)
print("AFTER")
print(x)

x = [1,2,3,4,5]
x[0],x[-1]=x[-1],x[0]
print(x)

print("TASK 3")

x = int(input("Enter number of elements : "))

y = []
z=[]
 
for i in range(x):
    element = int(input())
    y.append(element) 
print(y)
for i in range(x):
    element = int(input())
    z.append(element) 
print(z)

y[1],y[3]=z[1],z[3]

print(y)


list = [1,2,3,4,5,6]

for i in list:
    if(i==8):
        print("TRUE")
    elif(i!=8):
        print("FALSE")




print("TASK 4") 

REVERSING A LIST IN PYTHON WITHOUT REVERSE METHOD :


x = [4,5,6,7,8,9]
x[0],x[-1]=x[-1],x[0]
x[1],x[-2]=x[-2],x[1]
x[2],x[-3]=x[-3],x[2]
print(x)

