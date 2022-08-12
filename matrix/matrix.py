M = list[list[int]]


def mul(a: M, b: M) -> M:
    # (n,k) * (k, m) -> (n, m)
    n = len(a)
    k = len(a[0])
    m = len(b[0])
    c = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for x in range(k):
                c[i][j] += a[i][x] * b[x][j]
    return c


def pow(a: M, n: int) -> M:
    # (m, m)
    m = len(a)
    acc = [[0] * m for _ in range(m)]
    for i in range(m):
        acc[i][i] = 1

    while n:
        if n & 1:
            acc = mul(acc, a)
        a = mul(a, a)
        n >>= 1
    return acc
