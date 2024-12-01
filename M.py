import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def collatz_length(n):
    length = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

# Calculate lengths for numbers 1 to 1M
N = 1_000_000
lengths = [collatz_length(i) for i in range(1, N + 1)]

# Count multiplicities
counter = Counter(lengths)
unique_lengths = sorted(counter.keys())
multiplicities = [counter[length] for length in unique_lengths]

# Calculate statistics
mean_length = np.mean(lengths)
std_dev = np.std(lengths)

# Create the plot
plt.figure(figsize=(12, 6))
plt.bar(unique_lengths, multiplicities, width=1, alpha=0.7)
plt.axvline(x=mean_length, color='r', linestyle='--', label=f'Mean: {mean_length:.2f}')
plt.axvline(x=mean_length + std_dev, color='g', linestyle=':', label=f'Std Dev: ±{std_dev:.2f}')
plt.axvline(x=mean_length - std_dev, color='g', linestyle=':')

plt.xlabel('Sequence Length')
plt.ylabel('Multiplicity')
plt.title('Multiplicities of Collatz Sequence Lengths')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('collatz_multiplicities.png', dpi=300, bbox_inches='tight')
plt.close()
