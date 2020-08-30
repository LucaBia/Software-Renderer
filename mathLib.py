
# ----------------------
# Librerias matematicas
# ----------------------
# Suma de vectores de 3 elementos
def sum(x0, x1, y0, y1, z0, z1):
    arr_sum = []
    arr_sum.extend((x0 + x1, y0 + y1, z0 + z1))
    return arr_sum

# Resta de vectores de 3 elementos
def sub(x0, x1, y0, y1, z0, z1):
    arr_sub = []
    arr_sub.extend((x0 - x1, y0 - y1, z0 - z1))
    return arr_sub

def sub2(x0, x1, y0, y1):
    arr_sub = []
    arr_sub.extend((x0 - x1, y0 - y1))
    return arr_sub

def subVectors(vec1, vec2):
    subList = []
    subList.extend((vec1[0] - vec2[0], vec1[1] - vec2[1], vec1[2] - vec2[2]))
    return subList
    
# Producto cruz entre dos vectores
def cross(v0, v1):
    arr_cross = []
    arr_cross.extend((v0[1] * v1[2] - v1[1] * v0[2], -(v0[0] * v1[2] - v1[0] * v0[2]), v0[0] * v1[1] - v1[0] * v0[1]))
    return arr_cross

# Producto punto (utilizado para la matriz con las coordenadas de luz)
def dot(norm, lX, lY, lZ):
    return ((norm[0] * lX) + (norm[1] * lY) + (norm[2] * lZ))

# Calculo de la normal de un vector
def norm(v0):
    if (v0 == 0):
        arr0_norm = []
        arr0_norm.extend((0,0,0))
        return arr0_norm

    return((v0[0]**2 + v0[1]**2 + v0[2]**2)**(1/2))

def frobeniusNorm(norm):
        return((norm[0]**2+norm[1]**2+norm[2]**2)**(1/2))

# Division vector con normal
def div(v0, norm):
    if (norm == 0):
        arr0_norm = []
        arr0_norm.extend((0,0,0))
        return arr0_norm
    else:
        arr_div = []
        arr_div.extend((v0[0] / norm, v0[1] / norm, v0[2] / norm))
        return arr_div

# Crea una matriz llena de ceros
def zeros_matrix(rows, cols):
    m = []
    while len(m) < rows:
        m.append([])
        while len(m[-1]) < cols:
            m[-1].append(0.0)

    return m

# Multiplicacion de dos matrices
def matrix_multiply(m1, m2):
    rowsM1 = len(m1)
    colsM1 = len(m1[0])
    colsM2 = len(m2[0])
 
    c = zeros_matrix(rowsM1, colsM2)
    for i in range(rowsM1):
        for j in range(colsM2):
            total = 0
            for k in range(colsM1):
                total += m1[i][k] * m2[k][j]
            c[i][j] = total
 
    return c

# Multiplicacion de un vector con una matriz
def multiplyVM(v, m):
    result = []
    for i in range(len(m)):
        total = 0
        for j in range(len(v)):
            total += m[i][j] * v[j]
        result.append(total)
    return result  

def degToRad(number):
    pi = 3.141592653589793
    return number * (pi/180)

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("MATRIX NOT INVERTIBLE")
                return -1
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def multiply(dotNumber, normal):
    arrMul = []
    arrMul.extend((dotNumber * normal[0], dotNumber * normal[1], dotNumber * normal[2]))
    return arrMul




# def baryCoords(A, B, C, P):
#     # u es para la A, v es para B, w para C
#     try:
#         u = ( ((B[1] - C[1])*(P[0] - C[0]) + (C[0] - B[0])*(P[1] - C[1]) ) /
#               ((B[1] - C[1])*(A[0] - C[0]) + (C[0] - B[0])*(A[1] - C[1])) )

#         v = ( ((C[1] - A[1])*(P[0] - C[0]) + (A[0] - C[0])*(P[1] - C[1]) ) /
#               ((B[1] - C[1])*(A[0] - C[0]) + (C[0] - B[0])*(A[1] - C[1])) )

#         w = 1 - u - v
#     except:
#         return -1, -1, -1

#     return u, v, w

def baryCoords(Ax, Bx, Cx, Ay, By, Cy, Px, Py):
    # u es para la A, v es para B, w para C
    try:
        u = ( ((By - Cy)*(Px - Cx) + (Cx - Bx)*(Py - Cy) ) /
              ((By - Cy)*(Ax - Cx) + (Cx - Bx)*(Ay - Cy)) )

        v = ( ((Cy - Ay)*(Px - Cx) + (Ax - Cx)*(Py - Cy) ) /
              ((By - Cy)*(Ax - Cx) + (Cx - Bx)*(Ay - Cy)) )

        w = 1 - u - v
    except:
        return -1, -1, -1

    return u, v, w
# -------------------------------------------------------------