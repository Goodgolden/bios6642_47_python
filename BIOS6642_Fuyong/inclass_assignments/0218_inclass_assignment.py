n, m = 0, 100
even_number = 0
while n != m:
    n = int(input())
    if n%2 == 0:
        even_number += 1
    print("n =", n)
    if n < 0:
        break

print('How many even numbers?', even_number)
