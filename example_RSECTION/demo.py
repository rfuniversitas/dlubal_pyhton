#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
baseName = os.path.basename(__file__)
dirName = os.path.dirname(__file__)
print('basename:    ', baseName)
print('dirname:     ', dirName)
sys.path.append(dirName + r'/..')


from RSECTION.initModel import Model
from RSECTION.BasicObjects.point import Point


if __name__ == '__main__':

    Model(True, "Demo") # crete new model called Demo1
    Model.clientModel.service.begin_modification()

    # Point(1, 0.0, 0.02)
    # Point(2, 0.2, 0,0)
