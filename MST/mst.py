N = 1e5+10
parent = [None]* int(N)
size = [None]* int(N)

def make(v):
    parent[v] = v
    size[v] = 1


def find(v):
    if parent[v] == v:
        return parent[v]
    parent[v] =  find(parent[v])
    return (parent[v])

def Union(a, b):
    a = find(a)
    b = find(b)
    if (a != b):
        if(size[a] < size[b]):
            a, b = b, a
        parent[b] = a
        size[a] += size[b]



vE = input("Enter Total No. of vertices and edges: ").split()
edges = []
for i in range(int(vE[1])):
    xYWt = input("Enter vertices where edge is present with weight: ").split()
    edges.append((int(xYWt[0]),(int(xYWt[1]), int(xYWt[2]))))

totalCost = 0
edges.sort(key=lambda e: e[0])
for i in range(int(vE[0])):
    make(i)
print("***************************MST Edges********************************")
for i in range(len(edges)):
    wt, XY = edges[i]
    x = XY[0]
    y = XY[1]
    if (find(x) == find(y)):
        continue
    Union(x, y)
    totalCost += wt
    print( x, y)

print("Minimum Cost is : ", totalCost)

