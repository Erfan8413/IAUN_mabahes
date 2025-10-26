n = int(input("Enter a two-digit number: "))
sign = -1 if n < 0 else 1
if 10 <= n <= 99:
    rev = (n % 10) * 10 + n // 10
    print(sign * rev)
else:
    print("Error: The entered number is not a two-digit number")