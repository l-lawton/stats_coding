import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def prob_collatz_length(n, p=0.5):
    seen = set()
    length = 0
    current = n
    
    while True:
        if current == 1:
            return length
            
        if current in seen:
            return length
            
        seen.add(current)
        
        if current % 2 == 0:
            current = current // 2
        else:
            # Probabilistic choice between 3n+1 and 3n-1
            if np.random.random() < p:
                current = 3 * current + 1
            else:
                current = 3 * current - 1
        
        length += 1

# Calculate lengths for numbers 1 to 1M
N = 1_000_000
p = 0.5  # Probability for 3n+1
lengths = [prob_collatz_length(i, p) for i in range(1, N + 1)]

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
plt.title(f'Multiplicities of Probabilistic Collatz Sequence Lengths (p={p})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('prob_collatz.png', dpi=300, bbox_inches='tight')
plt.close()
