a=int(input())
b=int(input())
c=int(input())
def diff(a,b,c):
  if a>b>c:
    return a-c
  if a>c>b:
    return a-b
  if b>a>c:
    return b-c
  if b>c>a:
    return b-a
  if c>a>b:
    return c-b
  if c>b>a:
    return c-a
  else:
    return 0
 print (def(a,b,c))
