#coding:utf-8
# import pdb
import matplotlib;

matplotlib.use("Qt4Agg")
import matplotlib.pyplot as plt
from pattern.classify import classifyObject
from pattern.draw import output_axies_plot_to_dir, output_axies_plot_to_matplot
from util.getimg import randomImg


def ttest_output_axies_plot_to_dir():
    u"""unit test case for output_axies_plot_to_dir"""
    img = randomImg("IMG\\G652\\pk\\")
    classify = classifyObject("G652")
    result = classify.find(img)
    core = result['corecore']
    dir_ = 'tests\\data\\axies_plot.png'
    output_axies_plot_to_dir(core, img, dir_)


def test_output_axies_plot_to_matplot():
    """unit test case for output_axies_plot_to_matplot"""
    fig = plt.figure()
    img = randomImg("IMG\\G652\\pk\\")
    classify = classifyObject("G652")
    result = classify.find(img)

    core = result['corecore']
    x, h, y, v = output_axies_plot_to_matplot(core, img)
    ax1 = fig.add_subplot(111)
    # ax1.plot(x,h)
    # ax1.set_ylabel('bit')
    # ax2 = ax1.twinx()
    # ax2.plot(y,v,'r')
    # ax2.set_ylabel('bit')
    # ax2.set_xlabel('pix')
    # plt.show()


if __name__ == '__main__':
    test_output_axies_plot_to_matplot()
