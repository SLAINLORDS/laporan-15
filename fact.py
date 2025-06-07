def faktorial(n):
    if n==0 or n==1:
        return 1
    else:
        return faktorial(n-1) * n
print(faktorial(4))