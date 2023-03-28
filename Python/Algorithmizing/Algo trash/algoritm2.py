A = int(input())
B = int(input())


if A * A < 4 * B:
    print("No solution")
else:
    x1 = (A + (A * A - 4 * B) ** 0.5) / 2
    y1 = A - x1
    x2 = (A - (A * A - 4 * B) ** 0.5) / 2
    y2 = A - x2
    if x1 == x2 and y1 == y2: 
        print(f"X = {int(x1)}, Y = {int(y1)}")
    else:
        print(f"X = {int(x1)}, Y = {int(y1)}")
        print(f"X = {int(x2)}, Y = {int(y2)}")


