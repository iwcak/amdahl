import random

def generate_file(filename, count, max_val):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(str(random.randint(1, max_val)) + '\n')

generate_file('data/small.txt',    1000,    5000)
generate_file('data/medium.txt',  5000,  25000)
generate_file('data/large.txt', 20000, 100000)
