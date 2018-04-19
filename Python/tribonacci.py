def tribonacci(signature,n):
    for i in range(n-len(signature)):
        signature.append(signature[i] + signature[i+1] + signature[i+2])
    return signature[:n]
tribonacci([1,1,1],1)