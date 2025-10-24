num = int(input())
if num % 2 == 0 and num % 3 != 0:
    print("B")
elif num % 2 == 0 and num % 3 == 0:
    print("C")
else:
    print("D")