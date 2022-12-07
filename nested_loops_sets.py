loop = set()

loop = {(i, j) for i in range(3) if i % 2 == 0
              for j in range(4) if j % 2 == 1}

print(loop)