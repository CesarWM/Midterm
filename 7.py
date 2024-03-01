import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]
print(random_numbers)
