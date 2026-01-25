number = int(input("Input ur number: "))
digets = len(str(number))
resultnumber = 0
temp = number

while temp > 0:
    digit = temp % 10
    resultnumber += digit ** digets
    temp //= 10

if number == resultnumber:
    print(number, "is an armstrong number")

else:
    print(number, "is not an armstrong number")
