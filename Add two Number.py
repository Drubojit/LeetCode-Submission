nums = []
number_of_elements =int(input())
target = int(input())
for i in range(number_of_elements):
    temp = int(input())
    nums.append(temp)

for j in range(len(nums)):
    temp1 = nums[j]
    if j==len(nums)-1:
        exit()
    for k in range(j+1,len(nums)):
        if temp1+nums[k] == target:
            print(j,k)




