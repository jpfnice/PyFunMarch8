"""
Exercise 2:
    
Step 0: 
    Create an empty list "numbers"
    
Step 1: 
    Retrieve numbers one by one using the input() function and a loop.
    When the string "stop" will be provided it indicates the last number has    
    been given.
    Each number given will be stored into the list numbers.
    
Step 2:
    Print the list numbers
    
Step 3:
    Compute the minimum, the maximum and the average of the numbers stored in the list
    
Step 4:
    Compute the "truncated mean" of the numbers. The "truncated mean" takes into account all numbers except the smallest and largest ones:
    Ex: [1,2,1,4,5,2,3,6,6,4,3]
    -> [2,4,5,2,3,4,3] -> compute the mean
    
"""

numbers=[] # Step 0

# Step 1:
while True:
    answer=input("Enter an int or 'stop': ")
    if answer == "stop":
        break
    numbers.append(int(answer))
    
# Step 2:    
print(numbers)

# Step 3:
print("The minimum is:", min(numbers))
print("The maximum is:", max(numbers))
print("The average is:", sum(numbers)/len(numbers))

# OR
# [2, 3, 4, 2, 3, 4]
mini=numbers[0] # 2
maxi=numbers[0] # 4
total=numbers[0]# 18

for e in numbers[1:]: #[]
    if e < mini:
        mini=e
    if e > maxi:
        maxi=e
    total += e

print("The minimum is:", mini)
print("The maximum is:", maxi)
print("The average is:", total/len(numbers))

# Step 4:
    
print(numbers)
numbers.sort()

print(numbers)
idx1=numbers.count(numbers[0])

idx2=numbers.count(numbers[-1])

print(idx1, idx2)

subl1=numbers[idx1:len(numbers)-idx2]


print(sum(subl1)/len(subl1))
    
