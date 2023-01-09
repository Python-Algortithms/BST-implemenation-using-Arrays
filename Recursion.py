def SUM (a , n):
    if n == 0 : return a[0]
    return a[n] + SUM (a , n-1)

# using Binary Recursion
def BSUM(a , l , h): 
    if l >= h:return 0
    m = (l+h)//2
    return a[m] + BSUM(a,l,m) + BSUM(a,m+1,h)


a = [1,5,-1,2,4]
print(BSUM(a,0,len(a)))
