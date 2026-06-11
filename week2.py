# Linear Congruential Generator (LCG)

def lcg(seed, a=1664525, c=1013904223, m=2**32, n=20):
    numbers = []
    x = seed

    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)

    return numbers


seed = int(input("Enter seed value: "))
random_numbers = lcg(seed)

print("\nGenerated LCG sequence:")
for num in random_numbers:
    print(num)
