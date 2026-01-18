def ONSquareTime(n):
    iteration = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end="")
            iteration += 1
        
        print("")
    print("\nWhen n is :", n, "the total iterations done by code is:", iteration)

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\n With every n the time take increases by n^2")
print("O(n^2)")