def countdown(n):
    print("Enering functon n=" , n)

    if n == 0:
        print("Reached 0 stop recursion")
        return
    
    countdown(n-1)
    print("Existinf function n=" , n)

print("program started")

countdown(5)

print("program ended")