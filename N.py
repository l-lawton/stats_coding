import numpy as np
import matplotlib.pyplot as plt

def modified_collatz_length(n):
    seen = set()
    path = []
    length = 0
    current = n
    
    while True:
        path.append(current)
        
        if current == 1:
            return length, "blue"  # Path reaches 1
        
        if current in seen:
            return length, "red"   # Path forms a loop
            
        seen.add(current)
        
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current - 1
        
        length += 1

# Calculate lengths for numbers 1 to 1M
N = 1_000_000
results = [modified_collatz_length(i) for i in range(1, N + 1)]
lengths = [r[0] for r in results]
colors = [r[1] for r in results]

# Separate blue and red points
blue_indices = [i for i, c in enumerate(colors) if c == "blue"]
red_indices = [i for i, c in enumerate(colors) if c == "red"]
blue_lengths = [lengths[i] for i in blue_indices]
red_lengths = [lengths[i] for i in red_indices]

# Create the plot
plt.figure(figsize=(12, 6))
if blue_lengths:
    plt.plot([i+1 for i in blue_indices], blue_lengths, 'b.', 
             markersize=1, alpha=0.5, label='Paths to 1')
if red_lengths:
    plt.plot([i+1 for i in red_indices], red_lengths, 'r.', 
             markersize=1, alpha=0.5, label='Looping paths')

plt.xlabel('Integer n')
plt.ylabel('Sequence Length')
plt.title('Modified Collatz (3n-1) Sequence Lengths')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('modified_collatz.png', dpi=300, bbox_inches='tight')
plt.close()
