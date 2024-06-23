for i in range(10):
    if i == 2:
        print('i é 2, pulando')

    if i == 8:
        print('i é 8, seu else não executara')
        break

    for j in range(i, j):
        print(i, j)
else:
    print('For') 