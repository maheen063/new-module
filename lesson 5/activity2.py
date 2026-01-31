number_largest = int(input("Enter the larger number:"))
number_smallest = int(input("Enter the smaller number:"))

while (number_smallest):
    number_store = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = number_store

print("the HCF is:", number_largest)
