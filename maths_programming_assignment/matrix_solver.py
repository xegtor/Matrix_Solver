#Reading the number of rows, columns and reading the matrix
f = open("maths_programming_assignment/input.txt")
t = f.readline()
r = int(t[t.index("=")+2:])
t = f.readline()
c = int(t[t.index("=")+2:])
f.readline()
matrix = []
for i in range(r):
    g = list(map(float,f.readline().strip().split(" ")))
    matrix.append(g)
f.close()
if not matrix:
    print("TypeError : Invalid Matrix")
    exit()
z = []
for i in range(len(matrix)):
    if matrix[i].count(0) == c:
        z.append(i)
for i in range(len(z)):
    matrix.pop(z[i])
    r -= 1
    for j in range(i+1,len(z)):
        z[j] -= 1
if not matrix:
    print("Ax = 0 has infinite solutions")
    exit()
#sorting the matrix
for i in range(r):
    temp = []
    temp.extend(matrix)
    matrix = temp[:i]
    matrix.extend(sorted(temp[i:],key=lambda row: row[i:], reverse = True))
#reducing matrix to reduced row echelon form
for i in range(r):
    t = 0
    for k in range(c):
        if matrix[i][k] != 0:
            t += k
            break
    else:
        break
    for j in range(r):
        if i != j:
            mu  = matrix[j][t]/matrix[i][t]
            for k in range(t,c):
                matrix[j][k] = matrix[j][k] - matrix[i][k]*mu
for i in range(r):
    t = 0
    for k in range(c):
        if matrix[i][k] != 0:
            t = k
            break
    else:
        break
    for j in range(c-1,-1,-1):
        matrix[i][j] = matrix[i][j]/matrix[i][t]
for i in range(len(matrix)):
    for j in range(c):
        matrix[i][j] = round(matrix[i][j],4)
z = []
for i in range(len(matrix)):
    if matrix[i].count(0) == c:
        z.append(i)
for i in range(len(z)):
    matrix.pop(z[i])
    r -= 1
    for j in range(i+1,len(z)):
        z[j] -= 1
#sorting the matrix
for i in range(r):
    temp = []
    temp.extend(matrix)
    matrix = temp[:i]
    matrix.extend(sorted(temp[i:],key=lambda row: row[i:], reverse = True))
# making as et for all free varables
free_vars = set()
pviot_cols = set()
var = set()
for i in range(c):
    var.add(i)
for i in range(r):
    t = 0
    for k in range(c):
        if matrix[i][k] != 0:
            t = k
            break
    pviot_cols.add(t)
    for j in range(t+1,c):
        if matrix[i][j] != 0:
            free_vars.add(j)
for i in var:
    if i not in pviot_cols:
        free_vars.add(i)
if not free_vars:
    print("Ax = 0 only has trivial solution")
    exit()
# outputing the answer in parametric form
print("x = ",end="")
l = 0
for i in free_vars:
    t = []
    for j in range(r):
        t.append((-1)*matrix[j][i])
    l+=1
    for k in free_vars:
        if k == i:
            t.insert(k,1)
        else:
            t.insert(k,0)
    print(t,end="")
    print("x"+str(i+1),end="")
    if l != len(free_vars) and l != (len(free_vars)-1):
        print(" + ", end = "")
    elif l == (len(free_vars)-1):
        print(" + ")
    elif l == len(free_vars):
        print()