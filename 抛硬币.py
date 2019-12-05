import numpy as np

def random_one_number():
    return np.random.randint(0,2)

def main():
    sum_a = 0
    sum = 0
    for i in range(10000):
        a = random_one_number()
        b = random_one_number()
        if a == 1:
            sum += 1
        if a == 1 and b == 1:
            sum_a += 1
    print(sum_a/sum)


if __name__ == '__main__':
    main()