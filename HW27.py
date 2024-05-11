def geometric_progression(start, step):
    current = start
    while True:
        yield current
        current *= step


start_values = [-2, 10]
step_values = [-5, 3]

for start, step in zip(start_values, step_values):
    gen = geometric_progression(start, step)
    print(f"Геометрическая прогрессия с началом {start} и шагом {step}:")
    for _ in range(8):
        print(next(gen))
    print()
