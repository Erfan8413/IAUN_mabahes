n = int(input("Enter a two-digit number: "))
if 10 <= n <= 99:
    a = n // 10
    b = n % 10
    print(f"{a}^{b} =", a ** b)
    print(f"{b}^{a} =", b ** a)
else:
    print("Error: The entered number is not a two-digit number")