from RandomNumberGenerator import RandomNumberGenerator

def generate(n, Z):
    seed_gen = RandomNumberGenerator(Z)
    ai = []
    bi = []
    ri = []

    for i in range(n):
        ai.append(seed_gen.nextFloat(5, 35))
        bi.append(seed_gen.nextFloat(5, 35))
        ri.append(seed_gen.nextFloat(1, 4))
    x0 = seed_gen.nextFloat(5, 35)
    y0 = seed_gen.nextFloat(5, 35)

    return n, ai, bi, ri, x0, y0
