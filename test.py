import matplotlib.pyplot as plt
import numpy as np

def draw_boolean_array(arr):
    plt.figure(figsize=(6, 2))
    x = np.arange(len(arr))
    plt.bar(x, arr, color=['red' if v == 0 else 'green' for v in arr], edgecolor='black')
    plt.xticks(x)
    plt.yticks([0, 1])
    plt.ylim(-0.1, 1.1)
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Boolean Array Visualization")
    plt.show()

# Example usage
draw_boolean_array([0, 0, 1, 0, 1])
