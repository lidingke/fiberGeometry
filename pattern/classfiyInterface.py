from .classify import *

def classifyObject(fiberType):
    if fiberType == "octagon":
        from pattern.classify import OctagonClassify as Classify
    elif fiberType == "20400":
        from pattern.classify import Big20400Classify as Classify
    elif fiberType == "G652":
        print 'get new g652 classify'
        from pattern.classify import G652Classify as Classify
    else:
        from pattern.classify import G652Classify as Classify
    return Classify()
