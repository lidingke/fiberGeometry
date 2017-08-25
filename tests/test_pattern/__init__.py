
def assert_result(result,assert_ratio=0.9):
    core, clad = result['coreResult'], result['cladResult']
    print core['ellipese'], clad['ellipese'], result['cladResult'].keys()
    assert core['longAxisLen'] > 0.5
    assert core['shortAxisLen'] > 0.5
    assert core['longAxisLen'] > core['shortAxisLen']
    ratio = core['shortAxisLen'] / core['longAxisLen']
    assert ratio > assert_ratio

    # cv2.imshow("clad", clad['plot'][::4,::4])
    # cv2.waitKey()
    assert clad['longAxisLen'] > 0.5
    assert clad['shortAxisLen'] > 0.5
    assert clad['longAxisLen'] > clad['shortAxisLen']
    ratio = clad['shortAxisLen'] / clad['longAxisLen']
    assert ratio > assert_ratio