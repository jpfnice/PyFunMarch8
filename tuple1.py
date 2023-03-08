t1=(2,3,4,6,10)
print(t1, type(t1))
print(len(t1))
for e in t1:
    print(e)
    
t1=2,3,4,6,10
print(t1, type(t1))

t1=(2,)
print(t1, type(t1), len(t1))

t1=(2,3,4,6,10)
print(t1[0], t1[-1], t1[2:4])

l1=[67,78,90,67]
t1=tuple(l1)
print(t1)