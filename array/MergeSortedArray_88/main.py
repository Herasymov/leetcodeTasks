from solution import Solution as s
m=int(input())
n=int(input())
nums1=[]
for i in range(m+n):
    nums1.append(int(input()))
nums2=[]
for i in range(n):
    nums2.append(int(input()))
sol=s()
sol.merge(nums1,m,nums2,n)
print(nums1)
