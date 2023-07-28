e=[11,12,13,14,15]
x=bytearray(e)
print("Eg of Bytearray datatype")
print(x)
print(type(x))
print(x[0])
for i in x:
    print(i)
x[0]=80
x[1]=60
print("After updation:")
for i in x:
    print(i)
print("Eg of Byte datatype")
y=bytes(e)
print(y)
print(type(y))
for j in y:
    print(j)
