
# lists= []
# list0=[0,0,0]
# list1=[1,1]
# list2=[2]

# flist= list0+list1+list2
# print(flist)
# nums=[1,1,0]
# listt0=[]
# listt1=[]
# listt2=[]
# for i in range(0,len(nums)):
#     if nums[i]==0:
#         listt0.append(nums[i])
# for i in range(0,len(nums)):
#     if nums[i]==1:
#         listt1.append(nums[i])

# for i in range(0,len(nums)):
#     if nums[i]==2:
#         listt2.append(nums[i])

    
# final_list= listt0+listt1+listt2
# print( final_list)
# nums= [4,1,2,1,2]        
# dicc= {}
        
# counter= len(nums)
# for num in nums:
#     if num in dicc:
#         dicc[num]+=1
#     else:
#         dicc[num]=1
            
# for keys in dicc:
#     if dicc[keys]!=2:
#         n= keys
# print(n)

# nums1= [0]
# nums2= [1]

# for i in range(len(nums2)):
#     nums1.append(nums2[i])
#     nums1.remove(0)
    
# nums1.sort()    
# print(nums1)

name= "saeed"
typed= "ssaaedd"
diccname={}

dicctyped={}
for i in range(len(typed)):
    if typed[i] in name:
        if typed[i] in dicctyped:
            dicctyped[typed[i]]+=1
        else:
            dicctyped[typed[i]]=1
for i in range(len(name)):
    if name[i] in diccname:
        diccname[name[i]]+=1
    else:
        diccname[name[i]]=1
        
for key in dicctyped:
    if dicctyped[key]>=diccname[key]:
        cond=True
        continue
    else:
        cond= False
        break
print(cond)


        
        



