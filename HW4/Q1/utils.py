import numpy as np
import matplotlib.pyplot as plt

def U1(s1, s2):
    return s1 + 2*s2 + s1*s2 - s1**2

def U2(s1, s2):
    return 3*s2 + 3*s1 + s1*s2 - s2**2
    
s1_min, s1_max = 0.1, 3.1
s2_min, s2_max = 0.2, 3.2

def plot_graphs(s1_min, s1_max, s2_min, s2_max, BR1, BR2):
    eps1 = (s1_max-s1_min)/30
    eps2 = (s2_max-s2_min)/30
    fig, axes = plt.subplots(figsize=(5, 5))
    axes.grid(True)
    axes.plot([s2_min, s2_max], [BR1(s2_min), BR1(s2_max)], color='cyan', linewidth=1.7)
    axes.plot([BR2(s1_min), BR2(s1_max)], [s1_min, s1_max], color='magenta', linewidth=1.7)
    axes.plot([s2_min-eps2, s2_max+eps2], [s1_min, s1_min], '--', color='blue', linewidth=1)
    axes.plot([s2_min-eps2, s2_max+eps2], [s1_max, s1_max], '--', color='blue', linewidth=1)
    axes.plot([s2_min, s2_min], [s1_min-eps1, s1_max+eps1], '--', color='red', linewidth=1)
    axes.plot([s2_max, s2_max], [s1_min-eps1, s1_max+eps1], '--', color='red', linewidth=1)
    axes.set_xlabel('s2')
    axes.set_ylabel('s1')
    axes.legend(['BR1(s2)', 'BR2(s1)'])