N = int(input("Enter the number of prime numbers: "))

num = 2
prime = []

while len(prime) < N:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        prime.append(num)
    num += 1

print(prime)
