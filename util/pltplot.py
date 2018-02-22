#coding:utf-8
import matplotlib
matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt


def figure_plot(x,y,name='plot'):
    plt.figure(name)
    assert len(x) == len(y)
    plt.plot(x,y)
    plt.title(name)
    plt.show()

def twinx_figure_plot(x,y1,y2,name='plot'):
    fig = plt.figure(name)
    ax1 = fig.add_subplot(111)
    ax1.plot(x,y1)
    ax2 = ax1.twinx()
    ax2.plot(x,y2,color='red')
    # ax2.title(dir_)
    plt.show()