n = input("enter number: ")

max = 0
for ch in n:
    if ch.isdigit():       
        if int(ch) > max:
            max = int(ch)

print("max number: ", max)
