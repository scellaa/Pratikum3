# Initialize variable to store the largest number
largest = None
# Loop to prompt for input
while True:
    # Prompt user for input
    number = int(input("Enter a number (enter 0 to stop): "))
    
    # If input is 0, break the loop
    if number == 0:
        break
    
    # If this is the first input or the number is larger than current largest
    if largest is None or number > largest:
        largest = number
# Display the result
if largest is not None:
    print(f"The largest number is: {largest}")
else:
    print("No numbers were entered.")
