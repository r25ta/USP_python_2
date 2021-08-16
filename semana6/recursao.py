def x(n, m):
    if n == m or m == 0:
        return 1
    else:
        return x(n-1,m) + x(n-1,m+1)

def y(n):
    if n >= 0 or n <= 2:
        return n
    else:
        return y(n-1) + y(n-2) + y(n-3)

def z(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return z(n-1) + z(n-2) + z(n-3)
    
def w(n):
    if n == 0:
        print("<espaço A>")
    else:
        print("<espaço B>")
        w(n-1)
        print("<espaço C>")
    print("<espaço D>")
print("<espaço E>")
    
if __name__=="__main__":
#    print(x(5,3))
#    print(y(6))
#    print(z(6))
    w(10)