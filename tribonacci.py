def multiply(matrix1, matrix2): 
    MOD = 1000000007  
    a = ((matrix1[0][0] * matrix2[0][0]) % MOD + (matrix1[0][1] * matrix2[1][0]) % MOD + (matrix1[0][2] * matrix2[2][0]) % MOD) % MOD              
    b = ((matrix1[0][0] * matrix2[0][1]) % MOD + (matrix1[0][1] * matrix2[1][1]) % MOD + (matrix1[0][2] * matrix2[2][1]) % MOD) % MOD  
    c = ((matrix1[0][0] * matrix2[0][2]) % MOD + (matrix1[0][1] * matrix2[1][2]) % MOD + (matrix1[0][2] * matrix2[2][2]) % MOD) % MOD 
    
    d = ((matrix1[1][0] * matrix2[0][0]) % MOD + (matrix1[1][1] * matrix2[1][0]) % MOD + (matrix1[1][2] * matrix2[2][0]) % MOD) % MOD  
    e = ((matrix1[1][0] * matrix2[0][1]) % MOD + (matrix1[1][1] * matrix2[1][1]) % MOD + (matrix1[1][2] * matrix2[2][1]) % MOD) % MOD 
    f = ((matrix1[1][0] * matrix2[0][2]) % MOD + (matrix1[1][1] * matrix2[1][2]) % MOD + (matrix1[1][2] * matrix2[2][2]) % MOD) % MOD 
    
    g = ((matrix1[2][0] * matrix2[0][0]) % MOD + (matrix1[2][1] * matrix2[1][0]) % MOD + (matrix1[2][2] * matrix2[2][0]) % MOD) % MOD 
    h = ((matrix1[2][0] * matrix2[0][1]) % MOD + (matrix1[2][1] * matrix2[1][1]) % MOD + (matrix1[2][2] * matrix2[2][1]) % MOD) % MOD 
    i = ((matrix1[2][0] * matrix2[0][2]) % MOD + (matrix1[2][1] * matrix2[1][2]) % MOD + (matrix1[2][2] * matrix2[2][2]) % MOD) % MOD 
              
    matrix1[0][0] = a 
    matrix1[0][1] = b 
    matrix1[0][2] = c 
    matrix1[1][0] = d 
    matrix1[1][1] = e 
    matrix1[1][2] = f 
    matrix1[2][0] = g 
    matrix1[2][1] = h 
    matrix1[2][2] = i

def getTrib(trib, matrix):
    MOD = 1000000007
    a = ((trib[0][0] * matrix[0][0]) % MOD + (trib[1][0] * matrix[0][1]) % MOD + (trib[2][0] * matrix[0][2]) % MOD) % MOD
    b = ((trib[0][0] * matrix[1][0]) % MOD + (trib[1][0] * matrix[1][1]) % MOD + (trib[2][0] * matrix[1][2]) % MOD) % MOD
    c = ((trib[0][0] * matrix[2][0]) % MOD + (trib[1][0] * matrix[2][1]) % MOD + (trib[2][0] * matrix[2][2]) % MOD) % MOD

    trib[0][0] = a
    trib[1][0] = b
    trib[2][0] = c

def power(matrix, i):
    if (i == 0 or i == 1): 
        return
    M = [[ 1, 1, 1 ],  
         [ 1, 0, 0 ],  
         [ 0, 1, 0 ]]
    
    power(matrix, i // 2)
    multiply(matrix, matrix)

    if (i % 2): 
        multiply(matrix, M)

def solve(a,b,c,i):
    MOD = 1000000007

    A = a % MOD
    B = b % MOD
    C = c % MOD

    trib = [[C],  
         [B],  
         [A]]

    matrix = [[ 1, 1, 1 ],  
         [ 1, 0, 0 ],  
         [ 0, 1, 0 ]] 

    if i == 0:
        return A 
    elif i == 1:
        return B
    elif i == 2:
        return C
    else:
        power(matrix, i - 2)
        getTrib(trib, matrix)
    return trib[0][0]
        
a, b, c, i = list(map(int,input().rstrip().split(" ")))
print(solve(a,b,c,i))