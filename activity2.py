def count_once(n):
    count = 0
    for i in range(n):
        count += 1
    return count

def count_twice(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

n = 1000
print("Count once:", count_once(n))
print("Count twice:", count_twice(n))

def useing_variable(n):
    total = 0
    for i in range(n):
        total += i
    return total

def useing_lists(n):
    numbers = []

    for i in range(n):
        numbers.append(i)
    return sum(numbers)

print(useing_variable(1000))
print (useing_lists(1000))
