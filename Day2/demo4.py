list_of_numbers = input("Enter list of numbers seperated by ',': ")

list_of_numbers = list(map(int, list_of_numbers.split(',')))
print(f"Sum of Numbers is: {sum(list_of_numbers)}")
print(f"Average of Numbers is: {sum(list_of_numbers)/len(list_of_numbers)}")