print("welcome to the airport")
def airport():
    
    # Initialize an empty dictionary
    fly_list = {}

    # Get the number of entries
    num_of_tickets = int(input("how many tickets do you want to buy ?"))

    # Loop to get user input
    for _ in range(num_of_tickets):
        key = input("Enter name: ")
        value = input("Enter weight: ")
        num_value = float(value)  # Convert input to a number
        if num_value > 46:
            print("Not allowed to fly!")  # Warning message
            continue  # Skip adding this entry
    
        fly_list[key] = value  # Add key-value pair to dictionary

    # Print the final dictionary
    print("flight list:", fly_list)
    return fly_list
    
airport()

def delete_key(fly_list):
    line = input("Enter the key you want to delete: ")
    
    if line in fly_list :
        del fly_list [line]
        print(f"Key '{line}' deleted successfully!")
    else:
        print(f"Key '{line}' not found in the dictionary.")

delete_key()
    