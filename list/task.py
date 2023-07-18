
no = [1,2,3,4,5,6]
odd = []
even = []

for i in no:
    if(i %2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("Odd List",odd)
print("Even List",even)