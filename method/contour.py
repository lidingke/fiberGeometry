import cv2
import numpy as np
import pdb
from method.tree import NodeDict

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

    def run(self,img):
        contours, hierarchys = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        result = np.ones(img.shape)*255
        # for x in contours:
        print "next and previous contours at the same hierarchical level, the first child contour and the parent contour,"
        tree = NodeDict()
        for i,x in enumerate(contours):
            xhierar = hierarchys[0][i]
            area = cv2.contourArea(x)
            cvMom = cv2.moments(x)

            if cvMom['m00'] != 0.0:
                cvMomXY = (cvMom['m10']/cvMom['m00'],cvMom['m01']/cvMom['m00'])
                circleIndex = self._isCircle(area, cvMomXY, x)

                # if circleIndex > 0.8 and area >40:
                # if circleIndex > 0.4 and area >10:
                if area >10:
                    # print "area" , area , "circleIndex:", circleIndex,"mom:", cvMomXY, "hierar:", xhierar
                    # print "index", i,"area",area,\
                    #  "next area",cv2.contourArea(contours[xhierar[0]]),\
                    # "pre area",cv2.contourArea(contours[xhierar[1]]),\
                    # "child area",cv2.contourArea(contours[xhierar[2]]),\
                    # "parent area",cv2.contourArea(contours[xhierar[3]]), xhierar
                    # cv2.drawContours(result, x, -1, (0,0,255),maxLevel = 2)
                    tree[xhierar[3]] = i
                # cv2.drawContours(result, contours, 363, (0,0,255))
        # pdb.set_trace()
        # for key in tree.keys():
        #     print "key", key, "value", tree[key]
        tree.treeFilter()

        # tree.treeFilter()
        for key in tree.keys():
            # pdb.set_trace()
            print "key", key, "value", tree[key]
        print '----------------------'
        # tree.treeFilter()
        # pdb.set_trace()
        maxTree = tree.maxLenTree()
        maxTree.append(tree[maxTree[-1]][0])
        for key in maxTree:
            #
            print "key", key

            cv2.drawContours(result, contours[int(key)], -1, (0,0,255))
        # print
        # pdb.set_trace()

        cv2.imshow("img", result[::2,::2])
        cv2.waitKey(0)

class HoughCircles(find):
    """docstring for HoughCircles"""
    def __init__(self, ):
        super(HoughCircles, self).__init__()

    def run(self,img):
        para = 150
        circleMap = cv2.HoughCircles(image = img,
            method = cv2.cv.CV_HOUGH_GRADIENT,
            dp = 1,
            minDist = len(img)/8,#len(img)/8,
            param1 = 20,
            param2 = 10,
            minRadius = 0,
            maxRadius = 100)
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
            cv2.circle(img,(c0[0],c0[1]), c0[2], (255 ,0,0), 2)
        # pdb.set_trace()
        # if len(c0map) >10:
        #     c0map = c0map[4:-4]
        c0map.sort()
        circle = c0map[0]
        cv2.circle(img,(circle[1],circle[2]), circle[3], (0,255,0), 10)
        cv2.circle(self.origin,(circle[1],circle[2]), circle[3], (0,0,255), 4)
        # cv2.imwrite('result.jpg',self.origin)
        return img
