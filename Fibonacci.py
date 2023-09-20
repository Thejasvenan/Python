# Function to compute Fibonacci for a given number num
def Fibonacci(num):
    # Where F(0) is y and F(1) is x 
    y=0
    x=1
    
    # F is the F(num)
    F=0  
    if num==0:
        #F(0)=0
        return y
    elif num==1:
        #F(1)=1
        return x
        
    # For input n>=2
    elif num>=2:
        # Using iteration to continuousely computing the fibonacci
        for i in range(2,num+1):
        # F(n) = F(n-1) + F(n-2)
            F = x + y
        # For the next loop the values will interchange as follows
            y, x = x, F
        # After loop finished, final value of F is Fibonacci of num    
        return F

# Function to read the number n from the file.
def getNum(f):
    # number n is changed to int type when reading the file
    n=int(f.read())
    f.close()
    
    # Checking whether the n is in the input range or not
    if 0<=n<=20:
    # Returning the value n to the Function
        return n
        
    else:
    # For values n beyond the input range or other incompatible values.
        print("Invalid input!")
    return 

# Function to display the given value n and computed value F(n) on the screen.
def show(num):
# Print "Fibonacci(n) = F(n)" by calling function Fibonacci to compute the value
    print(f'Fibonacci({num}) =', Fibonacci(num))
    return 

# Function to write the text in a file
def saveFile(num):
    # Opening the required file in writing mode
    fo=open("result.txt", 'w')
    
    # Writing the same output displayed in above function
    fo.write(f'Fibonacci({num}) = {Fibonacci(num)}')
    
    # Closing the file to remember the written text
    fo.close()
    return

# Opening the file containing number in read mode by giving its name as input
fi=open(input(), "r")

# Calling getNum Function for fi file where 'a' gives the number n
a=getNum(fi)

# For n in correct input range, running the code
if a!=None:
    # Calling show Function to display the Fibonacci of n 
    show(a)
    
    # Calling saveFile Function to write the above displayed text in the "result.txt"
    saveFile(a)  
        
