def count_primes(num):
    count = 0
    for n in range(2, num):
        is_prime = True
        for i in range(2, n+1):
            if n % i == 0 and n != i:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


print(count_primes(10))  # 4
