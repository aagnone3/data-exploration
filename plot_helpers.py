import random
import matplotlib.pyplot as plt


def external_legend(ax, names):
    # shrink current axis's height by 10% on the bottom
    box = ax.get_position()
    ax.set_position([box.x0,
                     box.y0 + box.height * 0.1,
                     box.width,
                     box.height * 0.9])

    # put a legend below, in the space create by the axis shrink
    ax.legend(names, loc='upper center', bbox_to_anchor=(0.5, -0.05),
              fancybox=True, shadow=True, ncol=5)
    
    
def plot_format(title, xlabel, ylabel, grid=True):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(grid)
    
def random_colors(n_colors=1):
    return ["#%06x" % random.randint(0, 0xFFFFFF) for i in range(n_colors)]
