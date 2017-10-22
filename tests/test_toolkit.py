# from pattern.hist import CounterDict,getHist
# import matplotlib
# matplotlib.use("Qt4Agg")
import matplotlib.pylab as plt


# def test_counterdict():
#     mdlist = [1, 2, 2, 3, 4, 3, 3, 4, 5]
#     # pdb.set_trace()
#     md = CounterDict(max(mdlist) + 1)
#     md.append(mdlist)
#     assert len(md) == 6
#     assert md[3] == 3


# if __name__ == "__main__":
#     mdlist = [1, 2, 2, 3, 4, 3, 3, 4, 5]
#     # pdb.set_trace()
#     md = CounterDict(max(mdlist) + 1)
#     md.append(mdlist)
#     assert len(md) == 6
#     assert md[3] == 3


from GUI.model.stateconf import state_number


def test_state_number():
    sn = state_number()
    sns =  [next(sn)+1 for i in range(6)]
    assert sns == [1,2,3,4,5,1]

