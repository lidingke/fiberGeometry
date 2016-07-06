#!/usr/bin/python
import cv2
import numpy as np
import pdb

def find(file):
    pass

import sys
import os
if __name__ == '__main__':
    for file in os.listdir('img'):
        find = find("img\\"+file)
        find.run()
