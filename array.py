lis = []  
i = 0  

# Taking input from the user
while i < 5:
    a = int(input("Enter the element: "))  # Convert input to integer
    lis.append(a)  
    i += 1  

print("List:", lis)  

# Initializing sum to 0
sum = 0  
for x in range(len(lis)):  
    #sum = sum + lis[x]  
    sum += lis[x]

print("Sum of elements:", sum)
