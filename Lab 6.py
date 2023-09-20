#input dimension nxm
n,m=[int(x) for x in input("Enter the dimension: ").split(',')]
k=0 #condition to follow further process unless errors occured
#function for input 
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
        except : #for any other errors
            print("Error")
            k=2
            break
    return matrix
a=matrix("A") #Input Matrix A
if k==0: #running the code unless no errors
    b=matrix("B") #Input Matrix B
    if k==0:
        #Function to convert to Transpose
        def transpose(d):
            lis=[]
            T=[] #Transpose
            for i in range(m):
                for j in range(n):
                    lis.append(d[j][i])
                T.append(lis)
                lis=[]
            return T
        c=transpose(b)
        #Function for product of two matrices
        def multiply(e,f):
            matrixC=[] 
            for i in range(n):
                lin=[] #row of multiplied matrix
                for l in range(n):
                    add=0 #multiplication addition
                    for j in range(m):
                            add+=e[i][j]*f[j][l]
                    lin.append(add)
                matrixC.append(lin)
            return matrixC
        Result=multiply(a,c)
        #Function for displaying the Product of Matrices
        def output(mat):
            for i in mat:
                for j in i:
                    print(j, end=" ")
                print()
            return
        output(Result)
