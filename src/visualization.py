import matplotlib.pyplot as plt

def plot_exercise_map(exercise_map):
    x, y, c = [], [], []
    for i in range(exercise_map.shape[0]):
        for j in range(i + 1):
            x.append(i)
            y.append(j)
            c.append(exercise_map[i, j])
    _, ax = plt.subplots(figsize=(10, 6))
    sc = ax.scatter(x, y, c=c, cmap='coolwarm', s=100)
    ax.set_title("Early Exercise Map (American Call Option)")
    ax.set_xlabel("Time Step (i)")
    ax.set_ylabel("Upward Moves (j)")
    plt.colorbar(sc, label="1 = Exercise, 0 = Hold")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
