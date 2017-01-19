

class ClassCoreError(RuntimeError):

    def __init__(self):
        super(ClassCoreError, self).__init__()

class ClassOctagonError(RuntimeError):

    def __init__(self):
        super(ClassOctagonError, self).__init__()



class UnFindCorePoint(Exception):
    def __init__(self):
        super(UnFindCorePoint, self).__init__()