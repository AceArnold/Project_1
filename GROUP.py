import time
import sys
#FIRST PART
# 1. Syntax & Mutability
# List (Mutable)
my_list = [1, 2, 3]
my_list[0] = 10  # Can modify elements
print("List after modification:", my_list)

# Tuple (Immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error
print("Tuple remains unchanged:", my_tuple)

print("\n--- Iteration Speed ---")

# 2. Iteration Speed
large_list = list(range(1000000))
large_tuple = tuple(range(1000000))

# Measure iteration time for list
start_time = time.time()
for item in large_list:
    pass
print("List iteration time:", time.time() - start_time)

# Measure iteration time for tuple
start_time = time.time()
for item in large_tuple:
    pass
print("Tuple iteration time:", time.time() - start_time)

print("\n--- Memory Consumption ---")

# 3. Memory Consumption
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print("List size:", sys.getsizeof(my_list))
print("Tuple size:", sys.getsizeof(my_tuple))

print("\n--- Built-in Methods ---")

# 4. Built-in Methods
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# List methods
my_list.append(4)
print("List after append:", my_list)

# Tuple methods (only count & index)
print("Tuple count of 1:", my_tuple.count(1))
print("Index of 2 in tuple:", my_tuple.index(2))




#SECOND PART
# Create a set
# Create two empty sets
set1 = set()
set2 = set()

# Function to populate sets and perform set operations
def compare_sets():
    global set1, set2
    ask=int(input("how many students are in a class?"))

    # Populate set1
    set1 = set()

    for _ in range(ask):
        name = input("Enter a name in class A: ")
        set1.add(name)

    print("CLASS A:", set1)

    # Populate set2
    set2 = set()

    for _ in range(ask):
        name = input("Enter a name in class B: ")
        set2.add(name)

    print("CLASS B:", set2)
   
    # Perform set operations
    union_set = set1 | set2  # Union
    intersection_set = set1 & set2  # Intersection
    difference_set = set1 - set2  # Difference (set1 - set2)
    symmetric_difference_set = set1 ^ set2  # Symmetric Difference (Exclusive)
    
    # Print results
    print("CLASS A:", set1)
    print("CLASS B:", set2)
    print("STUDENTS IN ALL CLASSES:", union_set)
    print("STUDENTS IN BOTH CLASSES:", intersection_set)
    print("STUDENTS IN CLASS A BUT NOT IN CLASS B:", difference_set)
    print("STUDENTS IN ONLY ONE CLASS:", symmetric_difference_set)

# Run the function
compare_sets()
