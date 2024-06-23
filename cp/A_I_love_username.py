n= int(input())
sn= input().split()

num_a= [int(num) for num in sn ]

curr_min = num_a[0]
curr_max = num_a[0]
solution = 0

for index in range(1,n):
    number = num_a[index]
    
    if number < curr_min:
        solution += 1
        curr_min = number
        
    if number > curr_max:
        solution += 1
        curr_max = number
        
print(solution)
        
