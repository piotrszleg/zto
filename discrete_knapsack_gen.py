from RandomNumberGenerator import RandomNumberGenerator

def generate(n, Z):
    seed_gen = RandomNumberGenerator(Z)
    c_i = []
    w_i = []

    for i in range(n):
        c_i.append(seed_gen.nextInt(1, 30))
        w_i.append(seed_gen.nextInt(1, 30))
    B = seed_gen.nextInt(5*n, 10*n)

    return n, B, w_i, c_i