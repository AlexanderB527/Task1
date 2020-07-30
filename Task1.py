def odometer(oksana):
    rast=0
    z=oksana[:len(oksana):2]
    k=oksana[1:len(oksana):2]
    for i in range(len(z)):
        if i==0:
            rast=z[i]*(k[i])
        else:
            rast += z[i] * (k[i] - k[i-1])
    return rast
