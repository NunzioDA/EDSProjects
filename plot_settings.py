
from matplotlib import pyplot as plt


colors = ['#C88C27',  '#5C368E', '#BD4946', '#487DBA',  '#97B953', '#ff7f0e']
foreground = '#f7f7f7'
background = '#1f1f1f'
legend_color = '#2f2f2f'

theme_foreground = {
    'dark': '#f7f7f7',
    'light' : '#1f1f1f'
}

theme_background = {
    'dark': '#1f1f1f',
    'light' : '#f7f7f7'
}

theme_legend_color = {
    'dark': '#2f2f2f',
    'light' : '#ececec'
}

def set_theme(theme):
    global foreground, background, legend_color

    try:
        foreground = theme_foreground[theme]
        background = theme_background[theme]
        legend_color = theme_legend_color[theme]
    except:
        print("Wrong theme parameter: pass either 'dark' or 'light'.")
        print("Passed:", theme)


def title(title):
    plt.title(title, color=foreground)

def figure_ax():
    fig = plt.figure(facecolor=background)

    ax = fig.add_subplot(111)
    ax.set_facecolor(background)
    return fig, ax

def figure(figsize=None):
    return plt.figure(facecolor=background, figsize=figsize)

def subplot(nrow,ncol,index, xlabel='x', ylabel='y'):
    ax = plt.subplot(nrow,ncol,index)
    ax.set_facecolor(background)
    set_plot_theme(ax, xlabel=xlabel, ylabel=ylabel, show_legend=False)
    return ax

def color(Index):
    if len(colors)>Index:
        return colors[Index]
    else:
        return None

def legend():
    plt.legend(facecolor=legend_color, labelcolor=foreground,edgecolor="none")

def set_plot_theme(ax, xlabel='x', ylabel='y', show_legend=True):
    ax.set_xlabel(xlabel, color=foreground,)
    ax.set_ylabel(ylabel, color=foreground,)
    ax.tick_params(axis='x', which='both', labelcolor=foreground, color=foreground)
    ax.tick_params(axis='y', which='both', labelcolor=foreground, color=foreground)
    ax.spines['top'].set_color(foreground)     
    ax.spines['right'].set_color(foreground)    
    ax.spines['bottom'].set_color(foreground) 
    ax.spines['left'].set_color(foreground) 

    if show_legend:
        legend()