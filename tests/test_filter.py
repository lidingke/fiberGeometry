from util.load import WriteReadJson
from util.filter import MedianFilter
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

