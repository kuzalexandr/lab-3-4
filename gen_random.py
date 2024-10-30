import random
def gen_random(num_count, begin, end):
    for chr in range(num_count):
        yield random.randint(begin, end)

