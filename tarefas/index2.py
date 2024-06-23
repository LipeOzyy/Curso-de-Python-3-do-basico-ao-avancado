while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if m > n:
        m, n = n, m
    soma = 0
    print(f"{m}", end="")
    for i in range(m+1, n+1):
        print(f" {i}", end="")
        soma += i
    print(f" Sum={soma}")
