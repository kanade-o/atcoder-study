N = int(input())
l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in l:
    wari = 2**i
    print((N // wari) % 2, end="")

print("")
