import random
def gen_random(num_count, begin, end):

    result = [random.randint(begin, end) for i in range(num_count)]
    return result

print(gen_random(7, 1, 5))