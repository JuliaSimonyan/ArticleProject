import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import timeit
from cluster import cluster_snippets
from example import bubble_sort, factorial
from optimize import factorial_memo

def apply_optimizations(snippets, clusters):
    return snippets  

def plot_results():
    snippets = [bubble_sort, factorial]
    clusters = cluster_snippets(snippets)
    optimized_snippets = apply_optimizations(snippets, clusters)

    results = []
    for snippet in snippets:
        if snippet.__name__ == 'factorial':
            original_time = timeit.timeit(lambda: snippet(5), number=1000)
        else:
            original_time = timeit.timeit(lambda: snippet([64, 34, 25, 12, 22, 11, 90]), number=1000)
        results.append({'Function': snippet.__name__, 'Optimization': 'Original', 'Time': original_time})

    for snippet in optimized_snippets:
        if snippet.__name__ == 'factorial':
            optimized_time = timeit.timeit(lambda: snippet(5), number=1000)
        else:
            optimized_time = timeit.timeit(lambda: snippet([64, 34, 25, 12, 22, 11, 90]), number=1000)
        results.append({'Function': snippet.__name__, 'Optimization': 'Optimized', 'Time': optimized_time})

    results_df = pd.DataFrame(results)

    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    sns.barplot(data=results_df, x='Function', y='Time', hue='Optimization', ax=ax)
    ax.set_title('Execution Time of Functions Before and After Optimization')
    ax.set_xlabel('Function')
    ax.set_ylabel('Time (seconds)')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Optimization Results")

button = ttk.Button(root, text="Show Results", command=plot_results)
button.pack(pady=10)

root.mainloop()
