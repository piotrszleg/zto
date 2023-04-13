from docplex.mp.model import Model
import time

from discrete_knapsack_gen import generate

data = [generate(i, i) for i in range(2, 200)]

n_values = []
solving_times = []

for n, B, values, weights in data:
    m = Model(name='discrete_knapsack')

    x = []
    for i in range(0, n):
        x.append(m.binary_var(name='x{0}'.format(i)))

    weights_sum = m.sum(x[i]*weights[i] for i in range(n))
    m.add_constraint(weights_sum <= B)

    m.maximize(m.sum(x[i]*values[i] for i in range(n)))

    start = time.time()
    m.solve(log_output=False)
    end = time.time()

    # m.print_information()
    # m.print_solution()

    n_values.append(n)
    solving_times.append(end - start)

print("n, t")
for n, solving_time in zip(n_values, solving_times):
    print(f"{n}, {solving_time:.3f}")
