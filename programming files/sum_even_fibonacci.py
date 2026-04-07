# Initial terms of fibonacci sequence (1,1 would also work)
a, b = 0, 1

# accumulator for the sum of all even values in the fibonacci sequence
sum_even = 0

# keep going until the term in the fibonacci sequence is >= 4 million
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
