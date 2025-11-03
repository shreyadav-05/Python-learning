#    
"""
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
"""
n = 5  # number of rows

for i in range(1, n + 1):
    # spaces print karo
    print("  " * (n - i), end="")

    # increasing part
    for j in range(i, 2 * i):
        print(j, end=" ")

    # decreasing part
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")

    print()  # next line
