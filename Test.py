# print("Hello world")
A = [2, 4, 6, 8, 10, 12]
# print(type(A))
for s in A:
    print(s)

print(id(A))

B = A
print(A is B)
print(type(B))

C = A.copy()
print(C)
C[-1]=55
print(C)
print(len(C))
K = list(range(10, 0, -3))
print(K)
#print(dir(K))
#help(K.count)
print(K.count(2))






