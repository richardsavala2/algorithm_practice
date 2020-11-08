def add_integers(n):

    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)
        n = int(n/10)

    return sum
n = 987654309876543876543345678765434567898758237084978470897082475092398765434567876543234386756459896
print(add_integers(n))