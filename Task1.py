def squirrel(N):
    fact = 1
    for i in range(1,N+1):
        fact*=i
    k=str(fact)[0]
    return abs(k)