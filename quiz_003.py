N=()
result=""
counter=0
for i in range(100):
  result+=str(counter)+","
  if counter>=N:
    counter=0
   else:
    counter+1
