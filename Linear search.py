arr1 = [1, 1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 4, 5, 6]

arr3 = sorted(arr1 + arr2)  # Merge and sort

l = 0
for r in range(1, len(arr3)):
    if arr3[r] != arr3[l]:
        l += 1
        arr3[l] = arr3[r]

# The unique portion is arr3[:l+1]
print(arr3[:l+1])
arr=[0,3,1,4]
n=len(arr)
sum=sum(arr)
result=n * (n+1)//2
total=result-sum
print(total)
arr=[1,1,0,1,0,1,1,1,0]
def max_consecutive_ones(arr):
    max_count = 0
    count = 0
    
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0  # reset when we see a 0
    
    return max_count
print("max consecutive ones are :",max_consecutive_ones(arr))
def single_num(nums):
    for num in nums:
        if nums.count(num)==1:
            return num
nums=[1,1,2,2,3,4,4]
print("single appearance is:",single_num(nums))
nums=[1,1,2,3,3,4,4]
def single_number(nums):
    x = 0
    for n in nums:
        x ^= n
    return x
print("single appearance is:",single_number(nums))



 





