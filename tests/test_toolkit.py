from pattern.hist import CounterDict,getHist
import matplotlib.pylab as plt


def test_counterdict():
    mdlist = [1, 2, 2, 3, 4, 3, 3, 4, 5]
    # pdb.set_trace()
    md = CounterDict(max(mdlist) + 1)
    md.append(mdlist)
    assert len(md) == 6
    assert md[3] == 3


# if __name__ == "__main__":
#     mdlist = [1, 2, 2, 3, 4, 3, 3, 4, 5]
#     # pdb.set_trace()
#     md = CounterDict(max(mdlist) + 1)
#     md.append(mdlist)
#     assert len(md) == 6
#     assert md[3] == 3

if __name__ == '__main__':
    mdlist = [1,2,2,3,4,3,3,4,5]
    # pdb.set_trace()
    imhf = getHist(mdlist)
    # print imhf
    plt.plot(imhf)
    plt.show()