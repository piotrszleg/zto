from inspection_gen import generate
from docplex.mp.model import Model
import time

data = [generate(2**i, i) for i in range(2, 50)]

n_values = []
solving_times = []

def distance_square(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx*dx + dy*dy

for n, ai, bi, ri, x0, y0 in data:
    m = Model(name='inspection')

    x = []
    y = []
    for i in range(n):
        x.append(m.continuous_var(name='x{0}'.format(i)))
        y.append(m.continuous_var(name='y{0}'.format(i)))

    # minimize distances between waypoints 
    m.minimize(distance_square(x0, y0, x[0], y[0])+distance_square(x[-1], y[-1], x0, y0)
               +m.sum(distance_square(x[i], y[i], x[i+1], y[i+1]) for i in range(n-1)))

    # each waypoint needs to be inside of its circle 
    for i in range(n):
        constraint = distance_square(x[i], y[i], ai[i], bi[i])
        m.add_constraint(constraint <= ri[i]*ri[i])

    start = time.time()
    m.solve(log_output=False)
    end = time.time()

    # m.print_information()
    # m.print_solution()

    n_values.append(n)
    solving_times.append(end - start)

print("n, t")
for n, solving_time in zip(n_values, solving_times):
    print(f"{n}, \t{solving_time:.3f}")
