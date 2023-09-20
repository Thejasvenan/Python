# Function for input matrix
def matrix(C):
    global k
    print(f"Enter Matrix {C}:") #asking for the matrix
    matrix=[]
    for i in range(n):
        try:
            lis=[int(a)  for a in input().split()] #input separated by white space
            matrix.append(lis)
            if len(lis)!=m: #if number of elements is not equal to number of columns
                    print("Invalid Matrix")
                    k=1
                    break
            lis=[]
        except ValueError: #for any other errors
            print("Error")
            k=2
            break
    return matrix
# Function to convert to Transpose
def transpose(d):
    lis=[]
    T=[] #Transpose
    for i in range(m):
        for j in range(n):
            lis.append(d[j][i])
        T.append(lis)
        lis=[]
    return T
# Function to find Determinant
def determinant(a):
    if len(a)!=len(a[0]):
        print('This is not a Square matrix')
        return
    else:
        if len(a)==2:
            return (a[0][0]*a[1][1]-a[0][1]*a[1][0])
        elif len(a)==1:
            return (a[0][0])
        else:
            det=0
            col=len(a[0])
            row=len(a)
            for j in range(col):
                coef=(-1)**j
                b=a[0][j]
                sub_mat=[[a[i][k] for k in range(col) if k!=j] for i in range(1,row)]
                det+=coef*b*determinant(sub_mat)
            return det
# Function to find Adjoint
def adjoint(e):
    if len(e)==2:
        mat=[[e[i][j] for j in range(-1,-3,-1)] for i in range(-1,-3,-1)]
    else:
        mat=[]
        for l in range(len(e)):
            comat=[]
            for k in range(len(e[0])):
                sub=[[e[i][j] for j in range(len(e[0])) if j!=k] for i in range(len(e)) if i!=l]
                c=(-1)**(l+k)
                comat.append(c*determinant(sub))
            mat.append(comat)
    return(transpose(mat))
# Function to print inverse of matrix
def inverse(a):
    d=determinant(a)
    if d!=0:
        f=1/d
        m=adjoint(a)
        print("Inverse of Matrix A:")
        for i in m:
            for j in i:
                print(f*j, end=" ")
            print()
        return
    else:
        print("There's no inverse for this matrix")
        return                
# input dimension nxm
n,m=[int(x) for x in input("Enter the dimension: ").split(',')]
k=0 # condition to follow further process unless errors occured
a=matrix("A") #Input Matrix A
# if k==0: #running the code unless no errors
if k==0:
    inverse(a)
