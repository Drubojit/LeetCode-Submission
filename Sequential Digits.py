low = 1000
high = 13000

seq = []
for i in range(1,10,1):
    prev =str(i)
    for k in range(i+1,10):
         prev = prev+str(k)
         seq.append(prev)


final_result =[]
for x in seq:
     temp = int(x)
     if low<=temp<=high:
       final_result.append(temp)

final_result.sort()
print(final_result)