def prime_factors(n):
    i = 2
    # 2 is the smallest possible prime factor
    factors = []
    # list of factors to be printed out later
    while i * i <= n:
        # before you can just square i to make n
        if n % i:
            # if n /cannot/ be cleanly divided by i,
            i += 1
            # increment i by one, then try to divide by 3, 4, etc.
        else:
            # divide n/i and round down, aka flat division:
            n = n // i
            # then add i to the list
            factors.append(i)
            pass
        pass
    # now, if n is not yet zero, it's the last prime to add
    if n > 1:
        factors.append(n)
    return factors
    pass

n=int(input("Enter the number to be divvied:"))
print(prime_factors(n))