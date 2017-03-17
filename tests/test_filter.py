from util.load import WriteReadJson
from util.filter import MedianFilter, MedianLimitFilter, AvgResult
import numpy as np

def test_MedianFilter():
    jsobject = WriteReadJson("tests\\data\\light.json").load()
    medianget = MedianFilter(maxlen=5)
    result = []
    for x, y  in jsobject:
        medianget.append(x)
        print x,y,medianget.get()
        result.append((x,y,medianget.get()))
    npresult = np.array(result)
    assert npresult[::,0].std() > npresult[::,2].std()

def test_MedianLimitFilter():
    jsobject = WriteReadJson("tests\\data\\light.json").load()
    medianget = MedianLimitFilter(maxlen=5)
    result = []
    for x, y  in jsobject:
        # medianget.append(x)
        get = medianget.run(x)
        print x,y,get
        result.append((x,y,get))
    npresult = np.array(result)
    assert npresult[::,0].std() > npresult[::,2].std()


def test_avgresult():
    get = [[1,2,3],[2,3,4],[4,3,5],[7,6,2],[3,6,1]]
    result = AvgResult(get)
    print result
    assert [3.0,4.0,3.0] == result
