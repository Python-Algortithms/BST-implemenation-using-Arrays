def SUM (a , n):
    if n == 0 : return a[0]
    return a[n] + SUM (a , n-1)

# using Binary Recursion
def BSUM(a , l , h): 
    if l >= h:return 0
    m = (l+h)//2
    return a[m] + BSUM(a,l,m) + BSUM(a,m+1,h)


# The first ele >= target
def upper_bound (a,low,high,x):
 # 0 0 0 0 0 1 1 1 1 1 1 1 1
 if low >= high :
  return a[high]
 m = (low+high)//2
 if a[m] >= x :high = m
 else:low = m + 1
 return upper_bound (a,low,high,x)

if __name__ = '__main__':
 a = [1,3,5,9,11,22,60,80,100]
 ans = upper_bound(a,0,len(a)-1,x = 2)
 print(ans)
