
s1={2,3,4,5,16,-2,3,4} # curly braces
print(s1, len(s1), type(s1))

for e in s1:
    print(e)
    
s1.add(10)
print(s1, len(s1))

s1.remove(2)
print(s1, len(s1))

l1=[5,6,5,6,7]
s2=set(l1)
print(l1, s2)

print(s1.intersection(s2))