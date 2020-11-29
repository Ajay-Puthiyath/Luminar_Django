start =int(input("Enter the starting range"))
end = int(input("Enter the ending range"))

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)