def even_fibbs(limit):
    a, b = 0, 1
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a+b

print(sum(even_fibbs(4000000)))