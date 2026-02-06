d = dict()
d["Tetrahedron"]=4
d["Cube"]=6
d["Octahedron"]=8
d["Dodecahedron"]=12
d["Icosahedron"]=20
s= 0
for _ in range(int(input())):
    inp = input()
    s+=d[inp]
print(s)