import cv2
import numpy as np
import pdb
from method.tree import NodeDict
from method.toolkit import IsCircle, cv2CircleIndex, XlsWrite
# from method.toolkit import

class find(object):
    """docstring for find"""
    def __init__(self, ):
        super(find, self).__init__()
        # self.arg = arg

    def run(self,img):
        pass



class findContours(find):
    """docstring for findContours"""
    def __init__(self, ):
        super(findContours, self).__init__()
        # self.arg = arg
        self.circleIndex = cv2CircleIndex()

    def run(self,img):
        # pdb.set_trace()
        # what, contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape) * 255
        # print "next and previous contours at the same hierarchical level, the first child contour and the parent contour,"
        tree = NodeDict()

        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area , circleIndex = self.circleIndex.contourIn(x)
            if xhierar[2] == -1:
                # pdb.set_trace()
                print 'hieracrchys' ,i ,hierarchys[0][i]
            # if circleIndex > 0.8 and area >40:
            # if circleIndex > 0.4 and area >10:
            if area >10:
                tree[xhierar[3]] = i
        cv2.drawContours(result, contours, -1, (0,0,255))
        # pdb.set_trace()
        # for key in tree.keys():
        #     print "key", key, "value", tree[key]
        tree.treeFilter()

        # tree.treeFilter()
        for key in tree.keys():
            # pdb.set_trace()
            print "key", key, "value", tree[key]
        print '----------------------'
        maxTree = tree.maxLenTree()
        maxTree.append(tree[maxTree[-1]][0])
        # resultTree = []
        for key in maxTree[2:]:
            contour = contours[int(key)]
            area , index = self.circleIndex.contourIn(contour)

            print "key", key, area , index
            # if index > 0.7:
            #     resultTree.append(key)
            cv2.drawContours(result, contours[int(key)], -1, (0,255,255))
            temp = np.ones(img.shape)*255
            cv2.drawContours(temp, contours[int(key)], -1, (0,255,255))
            cv2.imshow("img", temp[::2,::2])
            cv2.waitKey(0)
        # pdb.set_trace()
        # print('result:',resultTree)
        return (img, result, contours, tree, maxTree, )

    def runNewTreeMethod(self,img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape) * 255
        # print "next and previous contours at the same hierarchical level, the first child contour and the parent contour,"
        # pdb.set_trace()
        fatherDot = set()
        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area , circleIndex = self.circleIndex.contourIn(x)
            # if xhierar[2] == -1:
                # pdb.set_trace()
                # print 'hieracrchys' ,i ,hierarchys[0][i]
            # xhierar[3]
            fatherDot.add(xhierar[3])
        print 'fatherdot', fatherDot

        for x in fatherDot:
            cv2.drawContours(result, contours[x], -1, (0,0,255))
        return img, result, contours, fatherDot

    def runNoThrowChirldMethod(self, img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape) * 255
        print 'before contour', hierarchys
        fatherDot = set()
        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area , circleIndex = self.circleIndex.contourIn(x)
            fatherDot.add(xhierar[3])
        print 'fatherdot', fatherDot
        for x in fatherDot:
            cv2.drawContours(result, contours[x], -1, (0,0,255))
        return img, result, contours, xrange(0, len(hierarchys[0]))


    def runCannyMethod(self,img):
        contours, hierarchys = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        result = np.ones(img.shape) * 255
        # print "next and previous contours at the same hierarchical level, the first child contour and the parent contour,"
        # pdb.set_trace()
        fatherDot = set()
        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area , circleIndex = self.circleIndex.contourIn(x)
            # if xhierar[2] == -1:
                # pdb.set_trace()
                # print 'hieracrchys' ,i ,hierarchys[0][i]
            # xhierar[3]
            fatherDot.add(xhierar[3])
        print 'fatherdot', fatherDot

        for x in fatherDot:
            cv2.drawContours(result, contours[x], -1, (0,0,255))
        return img, result, contours, fatherDot


class HoughCircles(find):
    """docstring for HoughCircles"""
    def __init__(self, ):
        super(HoughCircles, self).__init__()

    def run(self, img, origin ):
        self.origin = origin
        para = 150
        circleMap = cv2.HoughCircles(image = img,
            method = cv2.cv.CV_HOUGH_GRADIENT,
            dp = 1,
            minDist = len(img)/8,#len(img)/8,
            param1 = 20,
            param2 = 10,
            minRadius = 0,
            maxRadius = 300)
        c0map = []
        if circleMap is None:
            raise Exception('circle not find')
        for c0 in circleMap[0]:
            c01sum = []
            for c1 in circleMap[0]:
                diff = abs(c0[1]-c1[1])+abs(c0[0]-c1[0])
                c01sum.append(diff)
            c0map.append((sum(c01sum)/len(c01sum), c0[0], c0[1], c0[2]))
            # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            cv2.circle(self.origin,(c0[0],c0[1]), c0[2], (255 ,0,0), 2)
        # pdb.set_trace()
        # if len(c0map) >10:
        #     c0map = c0map[4:-4]
        c0map.sort()
        circle = c0map[0]
        # cv2.circle(img,(circle[1],circle[2]), circle[3], (0,255,0), 10)
        cv2.circle(self.origin,(circle[1],circle[2]), circle[3], (0,0,255), 4)
        # cv2.imwrite('result.jpg',self.origin)

        return self.origin


class FitEllipse(object):
    """docstring for FitEllipse"""
    def __init__(self, ):
        super(FitEllipse, self).__init__()
        # self.arg = arg
        self.circleIndex = cv2CircleIndex()

    def run(self, origin, result, contours, treeList):
        print 'tree:' , treeList
        isCircle = IsCircle()
        ellipseTree = []
        ellipseTreeforCircleIndexSort = []
        for x in treeList:
            if not (x == 0 or x == -1):
                result = cv2.fitEllipse(contours[int(x)])
                ellipseTree.append(result)
                print 'result:',x , result
        for circle in ellipseTree:
            cv2.ellipse(img = origin, box = circle, color=(0, 0, 255))
        # XlsWrite().savelist(ellipseTree)
        return origin

    def ellipseTreeforCircleIndexSort(self, origin, result, contours, treeList):
        # print 'tree:' , treeList
        isCircle = IsCircle()
        ellipseTree = []
        ellipseTreeforCircleIndexSort = []
        print 'tree', treeList
        for x in treeList:
            if not (x == 0 or x == -1):
                result = cv2.fitEllipse(contours[int(x)])
                ellipseTree.append(result)
                area , circleIndex = self.circleIndex.contourIn(contours[int(x)])
                result = tuple([circleIndex,area]) + self._coaxialityGet(result)
                ellipseTreeforCircleIndexSort.append(result)
        ellipseTreeforCircleIndexSort.sort()
        for x in ellipseTreeforCircleIndexSort:
            # pdb.set_trace()
            # pixSize = 2.2/20
            areaIndex = x[2]
            if areaIndex > 1:
                # pixSize = 2.2/20
                pixSize = 0.0886
                circleIndex = x[0]
                coaxiality = x[1] * pixSize
                radiusMin = x[3][1][0] * pixSize
                radiusMax = x[3][1][1] * pixSize
                radiusIndex = ((x[2]/3.14)**0.5) * pixSize
                print x[3]
                print "circleIndex: %8.4f, coaxiality: %8.4f, radiusMin: %8.4f, radiusMax: %8.4f, radiusIndex: %8.4f, %f"%(
                    circleIndex, coaxiality, radiusMin, radiusMax, radiusIndex, areaIndex)
        for circle in ellipseTree:
            cv2.ellipse(img = origin, box = circle, color=(0, 0, 255))
        # XlsWrite().savelist(ellipseTree)
        return origin

    def ellipseForIfCondition(self, origin, result, contours, treeList):
        isCircle = IsCircle()
        ellipseTree = []
        ellipseTreeforCircleIndexSort = []
        print 'tree', treeList
        for x in treeList:
            if not (x == 0 or x == -1):
                result = cv2.fitEllipse(contours[int(x)])
                ellipseTree.append(result)
                area , circleIndex = self.circleIndex.contourIn(contours[int(x)])
                result = tuple([circleIndex,area]) + self._coaxialityGet(result)
                ellipseTreeforCircleIndexSort.append(result)

        for circle in ellipseTree:
            cv2.ellipse(img = origin, box = circle, color=(0, 0, 255))

        return origin


    def runFromOldTree(self, origin, result, contours, treeList):
        print 'tree:' , treeList[ 2 : ]
        ellipseTree = []
        for x in treeList[2 : ]:
            result = cv2.fitEllipse(contours[int(x)])
            print 'result:', ellipseTree
        for circle in ellipseTree:
            cv2.ellipse(img = origin, box = circle, color = (0,0,255))
        return origin

    def _coaxialityGet(self, result):
        coaxiality = abs(result[1][0] - result[1][1])
        return (coaxiality, result)
