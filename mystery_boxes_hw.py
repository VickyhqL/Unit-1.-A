# #mystery box 1
a=input("Word here:")
def mb1(a):
  return a[::-1]
txt = mb1(a)
print(txt)

#mystery box 2
a=input("your email here:")
def mb2(a):
    return a.split("@")
b=mb2(a)
print(b)

#mystery box 3
#input 3 factors to give the LCM
a=int(input("Enter the factor 1:"))
b=int(input("Enter the factor 2:"))
c=int(input("Enter the factor 3:"))
def clcm(a,b,c):
   if c < a > b:
       greater = a
   if c<b>a:
       greater = b
   if b<c>a:
       greater = c
   while(True):
       if((greater % a == 0) and (greater % b == 0) and (greater % c == 0)) :
           lcm = greater
           break
       greater += 1

   return lcm
print(clcm(a,b,c))
  
a=(input())
b=a.split( )
def mb4(a):
    index=b.inedx()
    if index<7:
      print  mb4(a)
       
              return index![Screenshot (10)](https://user-images.githubusercontent.com/89110625/135782870-4cdd3a5a-8de8-4c87-a83f-eb6064577480.png)


  
